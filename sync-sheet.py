"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
import re
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint
from pathlib import Path

import logging
LOGGER = logging.getLogger("PWS")
logging.basicConfig(level=logging.INFO)

EPRIVACY_N = 'XXIV'

URL = 'e-privacy-'

PATH = 'content/2018/autumn/'


SESSIONI = (
    ("VENERDI_MATTINA", 0, 0, (
        ("Apertura", 'open', 'Venerdì!A2:J2'),
        ("Saluti", 'saluti', 'Venerdì!A3:J3'),
        ("Venerdì Mattina", 'talks', "Venerdì!A4:J8"),
        ("Tavola Rotonda", 'roundtable', 'Venerdì!A9:J9'),
        ("Pausa Pranzo", 'pausa', 'Venerdì!A10:J10'),
    )),
    ("VENERDI_POMERIGGIO", 0, 1, (
        ("Apertura", 'open', 'Venerdì!A16:J16'),
        ("Venerdì Pomeriggio", 'talks', "Venerdì!A17:J25"),
        ("Tavola Rotonda", 'roundtable', 'Venerdì!A26:J26'),
        ("Chiusura lavori prima giornata", 'pausa', 'Venerdì!A27:J27'),
    )),
    ("SABATO_MATTINA", 1, 0, (
        ("Sabato Mattina", 'talks', "Sabato!A2:J7"),
        ("Tavola Rotonda", 'roundtable', 'Sabato!A8:J8'),
        ("Chiusura lavori", 'pausa', 'Sabato!A9:J9'),
    )))


SHEET_HEADERS=(
    "label",
    "cron",
    "Cognome", "Nome", "X", "Organizzazione",
    "Indirizzo", "Email", "telefono",
    "Durata", "Argomento",
    "Titolo", "Autori",
    "Descrizione", "Bio",
    "Consenso_pubblicazione", "Consenso_registrazioni",
    "Note", "FullName")

def program_line(*cols):
    return " | ".join(cols)


def section_open(label, kind, srange, service, _id, info, rdb):
    lines = []
    for label, record in info.items():
        try:
            people = record['pres'].strip()
            if ',' in people:
                people = re.split(r', *', people)
            else:
                people = [people, ]
            names = make_persons(people, rdb)
            durata = re.sub(r'^0(|(0:))', '', record['Durata'])
            lines.append(program_line(record['Ora'],
                                      durata,
                                      names + "<br/>" + record['Titolo']))
        except:
            print("ERRORE: sulla linea {}".format(label))
            raise
    return lines, rdb


def section_saluti(label, kind, srange, service, _id, info, rdb):
    return section_open(label, kind, srange, service, _id, info, rdb)


def section_talks(label, kind, srange, service, _id, info, rdb):
    lines = []
    for label, record in sorted(info.items()):
        try:
            people = [record['pres'], ]
            if 'altri' in record and len(record['altri'].strip())>0:
                altri = re.split(r', *', record['altri'])
                people.extend(altri)
            for person in people:
                if person in rdb:
                    rdb[person]['talk'].append( record )
                else:
                    LOGGER.error('TALK: '+person+" non nel DB")
            names = make_persons(people, rdb)
            durata = re.sub(r'^0(|(0:))', '', record['Durata'])
            titolo = rdb[record['pres']]['Titolo']
            titolo = mk_intervento(titolo, record['pres']) 
            lines.append(program_line(record['Ora'],
                                      durata,
                                      names + "<br/>" + titolo ))
        except:
            print("ERRORE: sulla linea {}".format(label))
            raise
    return lines, rdb


def section_roundtable(label, kind, srange, service, _id, info, rdb):
    lines = []
    for label, record in sorted(info.items()):
        try:
            tavola = [record['pres'], ]
            people = re.split(r', *', record['altri'])
            modera = people.pop(0)
            if modera in rdb:
                record['role'] = 'moderatore'
                rdb[modera]['roundtable'].append( record )
            for person in people:
                if person in rdb:
                    rdb[person]['roundtable'].append( record )
                else:
                    LOGGER.error('TALK: '+person+" non nel DB")
            modera = make_persons([modera, ], rdb)
            names = make_persons(people, rdb)
            names = "Modera: "+modera+"<br/>Partecipano: "+names
            durata = re.sub(r'^0(|(0:))', '', record['Durata'])
            titolo = rdb[record['pres']]['Titolo']
            titolo = "Tavola Rotonda: " + mk_intervento(titolo, record['pres']) 
            lines.append(program_line(record['Ora'],
                                      durata,
                                      titolo + "<br/>" + names))
        except:
            print("ERRORE: sulla linea {}".format(label))
            raise
    return lines, rdb


def section_pausa(label, kind, srange, service, _id, info, rdb):
    lines = []
    for label, record in info.items():
        try:
            durata = re.sub(r'^0(|(0:))', '', record['Durata'])
            lines.append(program_line(record['Ora'],
                                      durata,
                                      record['Titolo']))
        except:
            print("ERRORE: sulla linea {}".format(label))
            raise
    return lines, rdb


def mk_md_link(nome, label, sezione, num=EPRIVACY_N):
    return "[_{nome}_](e-privacy-{num}-{sezione}.html#{label})".format(
        nome=nome, num=num, label=label, sezione=sezione
    )


def mk_relatore(nome, label, num=EPRIVACY_N):
    return "<span class='speaker'>"+mk_md_link(nome, label, 'relatori', num)+"</span>"


def mk_intervento(nome, label, num=EPRIVACY_N):
    return "<span class='talk'>"+mk_md_link(nome, label, 'interventi', num)+"</span>"


def format_relatori(relatori):
    md_relatori = []
    for relatore in re.split(';', relatori):
        md_relatori.append(mk_relatore(relatore))
    return ','.join(md_relatori)


FORMATS = (
    lambda label, x: x,
    lambda label, x: re.sub(r'^00:', '', x),
)

def make_authors(info, rdb):
    if 'pres' not in info:
        return ""
    pres = info['pres']
    if pres in rdb:
        record = rdb[pres]
    else:
        return ""
    org = ""
    if 'Organizzazione' in record and len(record['Organizzazione']) > 0:
        org = "({Organizzazione})".format(**record)
    di = "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome} {org}</a>".format(
        num=EPRIVACY_N,
        org=org,
        **record)
    if 'altri' in info and len(info['altri'])>0:
        altri = list(map(lambda x: x.strip(), re.split(',', info['altri'])))
        di += ", " + ", ".join(map(lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome} {org}</a>".format(
            num=EPRIVACY_N,
            **rdb[x],
            org=("("+rdb[x]['Organizzazione']+")") if 'Organizzazione' in rdb[x] and len(rdb[x]['Organizzazione']) > 0 else '',),
            altri))
        di = re.sub(r'(.*), ([^.]*)', '\\1 e \\2', di)
    return di

def make_authors_roundtable(info, rdb):
    if 'altri' in info and len(info['altri'])>0:
        altri = list(map(lambda x: x.strip(), re.split(',', info['altri'])))
        pres = altri.pop(0)
        if pres in rdb:
            record = rdb[pres]
        else:
            return ""
        org = ""
        if 'Organizzazione' in record and len(record['Organizzazione']) > 0:
            org = "({Organizzazione})".format(**record)
        di = "Modera: <a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome} {org}</a>".format(
            num=EPRIVACY_N,
            org=org,
            **record)
        di += "<br/>Partecipano: " + ", ".join(map(lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome} {org}</a>".format(
            num=EPRIVACY_N,
            **rdb[x],
            org=("("+rdb[x]['Organizzazione']+")") if 'Organizzazione' in rdb[x] and len(rdb[x]['Organizzazione']) > 0 else '',),
                                                   altri))
        di = re.sub(r'(.*), ([^.]+)$', '\\1 e \\2', di)
    return di


def read_db(service, id, range, HEADERS=SHEET_HEADERS):
    result = service.spreadsheets().values().get(spreadsheetId=id,
                                                 range=range).execute()
    values = result.get('values', [])
    infos = {}
    if not values:
        print('No data found.')
    else:
        for row in values:
            if len(row[0]):
                info = dict(zip(HEADERS, row))
                info['label'] = info['label'].lower()
                info['talk']=[]
                info['roundtable']=[]
                if 'pres' in info:
                    info['pres'] = info['pres'].lower()
                if 'altri' in info:
                    info['altri'] = info['altri'].lower()
                infos[info['label'].lower()] = info
    return infos


def read_programma_db(service, _id, rdb, SESSIONI):
    variables = {}
    db = {}
    J = 0
    K = 0
    for variable, J, K, sessione in SESSIONI:
        program = []
        db["{}.{}".format(J,K)] = {}
        LOGGER.info('SESSIONE '+variable)
        for label, kind, srange in sessione:
            LOGGER.info('    PARTE '+label)
            prog = read_db(service, 
                           _id, 
                           srange, 
                           HEADERS=('label', 'Giorno', 'Ora',
                                    'Durata', 'TECH', 'Titolo', 
                                    'Autore', 'pres', 'altri',
                                    'conferma'))
            db["{}.{}".format(J,K)].update(prog)
            func = "section_" + kind
            if func not in globals():
                raise SyntaxError('function {} ' 
                'not in globals()'.format(func))
            else:
                func = globals()[func]
            prglines, rdb = func(label, kind, srange, 
                            service, _id, prog, rdb)
            program.extend(prglines)
        variables[variable] = '\n'.join(program)
    return variables, rdb, db


def write_out(path, fname, **kw):
    templ_f = Path(path) / (fname+'.template')
    out_f = Path(path) / fname
    templ = templ_f.read_text(encoding='utf-8')
    output = templ.format(**kw)
    out_f.write_text(output)
    print("scrittura "+str(out_f)+" from template "+str(templ_f))


def setup_sheet_work(SPREADSHEET_ID):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service

def lay_talk(talk, item, db):
    pres = talk['pres']
    item = db[pres]
    titolo = item['Titolo']
    con = ""
    if titolo in db:
        titolo = db[titolo]['Titolo']
    if 'altri' in talk and len(talk['altri'])>0:
        label = item['label']
        altri = list(map(lambda x: x.strip(), 
                         re.split(',', talk['altri'])))
        altri.append(talk['pres'])
        if label in altri:
            altri.remove(label)
        if len(altri)>0:
            con = ", ".join(map(
                lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome}</a>".format(
                    num=EPRIVACY_N, **db[x.strip()]), altri))
        con = " con " + re.sub(r'(.*), ([^.]*)', '\\1 e \\2', con)
    return talk, titolo, con

def lay_roundtable(talk, item, db):
    label = talk['pres']
    con = ""
    titolo = db[label]['Titolo']
    ruolo = "Partecipa al"
    if 'altri' in talk:
        label = item['label']
        altri = list(map(lambda x: x.strip(), 
                         re.split(',', talk['altri'])))
        moderatore = altri.pop(0)
        if moderatore == label:
            ruolo = "Modera "        
        con = ", ".join(map(
            lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome}</a>".format(
                num=EPRIVACY_N, **db[x.strip()]), altri))
        con = " con " + re.sub(r'(.*), ([^.]*)', '\\1 e \\2', con)
    if ruolo == 'Partecipa al':
        con += " moderata da <a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome}</a>".format(num=EPRIVACY_N, **db[moderatore.strip()])
    return talk, ruolo, titolo, con

def make_speaker_bio(item,db):
    if 'Bio' in item and 'talk' in item:
        org = ""
        if 'Organizzazione' in item and \
        len(item['Organizzazione']) > 0:
            org = "(" + item['Organizzazione'] + ")"
        #if item['Titolo'] in db:
        #    item['talk'] = db[item['Titolo']]['talk']
        bio = '#### <a name="{label}"></a> {Nome} {Cognome} {org}\n\n{Bio}\n'.format(
            num=EPRIVACY_N,
            org=org, 
            **item )
        # <a href="/e-privacy-{num}-programma.html#{intervento}">⇧</a>
        #                 intervento=item['talk']['label'], 
        talks = []
        if 'talk' in item:
            for talk in item['talk']:
                talks.append(lay_talk(talk, item, db))

        if len(talks)>0:
            bio += "\nAd e-privacy " + EPRIVACY_N + " presenta <br/>\n"
            for talk, titolo, con in talks:
                bio += "<b><a href=\"e-privacy-{num}-interventi.html#{label}\">".format(num=EPRIVACY_N, label=talk['pres']) + titolo + "</a></b> alle <a href=\"/e-privacy-{num}-programma.html#{label}\">".format( num=EPRIVACY_N, label=talk['label']) + talk['Ora'] + " di " + talk['Giorno'] + "</a>" + con + ".<br/>"

        bio += "<br/>\n"
        roundtables = []
        if 'roundtable' in item:
            for roundtable in item['roundtable']:
                roundtables.append(lay_roundtable(roundtable, item, db))

        if len(roundtables)>0:
            # bio += "\nPartecipa alla " + ( "Tavola Rotonda" if len(roundtables) == 1 else "Tavole rotonde" ) + " <br/>\n"
            for talk, ruolo, titolo, con in roundtables:
                bio += "<br/>{ruolo}la Tavola Rotonda <b><a href=\"e-privacy-{num}-interventi.html#{label}\">".format(ruolo=ruolo,num=EPRIVACY_N, label=talk['pres']) + titolo + "</a></b> alle <a href=\"/e-privacy-{num}-programma.html#{label}\">".format(  num=EPRIVACY_N, label=talk['label']) + talk['Ora'] + " di " + talk['Giorno'] + "</a>" + con + ".<br/>\n\n"
        bio += '\n\n'
        return bio
        
def make_speakers(service, id, db):
    relatori = {}
    for key, item in db.items():
        LOGGER.info("MK-SPEAKER:"+key)
        rkey = item['Cognome'].capitalize()
        if rkey in ('Somma', 'Calamari'):
            continue
        relatori[rkey] = make_speaker_bio(item,db)
    str_out = ""
    for relatore in sorted(relatori.values()):
        str_out += relatore + "\n"
    write_out(PATH, 'speakers.md', RELATORI=str_out)


def make_interventi(service, id, db, pr):
    str_out = ""
    for day in pr.values():
        for key, item in day.items():
            LOGGER.info('TALK: ' + key)
            if 'pres' in item:
                pres = item['pres']
                if pres in db:
                    if re.match('^tavola',pres):
                        autori = make_authors_roundtable(item,db)
                    else:
                        autori = make_authors(item, db)
                    xdb = db[pres]
                    if 'Titolo' in xdb and len(xdb['Titolo'].strip())==0:
                        continue
                    if 'Descrizione' in xdb:                        
                        info = '#### <a name="{label}"></a> {Titolo} <a href="/e-privacy-{num}-programma.html#{intervento}">⇧</a>\n**{autori}**  \n\n{Descrizione}\n\n\n'.format(
                            num=EPRIVACY_N,
                            autori=autori,
                            intervento=item['label'],
                            **xdb)
                        str_out += info + "\n"
    write_out(PATH, 'interventi.md', INTERVENTI=str_out)

def make_tavolarotonda(item, db):
    pers = item['pres']
    record = db[pers]
    aList = re.split(r' *, *', record['Autori'])
    modera = aList.pop(0)
    modera = "Modera: " + make_person(modera, db)
    partecipa = "Partecipa: " + make_persons(aList, db)
    return "Tavola Rotonda: " + mk_intervento(record['Titolo'], pers) + "<br/>" + modera + "<br/>" + partecipa

def make_person(label, db):
    return make_authors(
        {'pres': label,
         'label': label},
        db)


def make_persons(aList, db):
    try:
        label = aList.pop(0)
        param = {'pres': label,
                 'label': label,
                 }
        if len(aList) > 0:
            param['altri'] = ','.join(aList)
        return make_authors(param, db)
    except IndexError:
        return ""


# def make_programma(service, id, db, pr):
#     str_out = []
#     for day in pr.values():
#         str_out_x = ""
#         for key, item in day.items():
#             item['Durata'] = re.sub('^0(0:)?', '', item['Durata'])
#             nocols = False
#             titolo = item['Titolo']
#             if titolo[0] == '*':
#                 nocols = True
#                 titolo = titolo[1:]
#             if 'pres' in item:
#                 titolo = "<a href='/e-privacy-{num}-interventi.html#{label}'>{titolo}</a>".format(
#                     num=EPRIVACY_N,
#                     label=item['pres'],
#                     titolo=titolo,
#                 )
#                 if re.match(r'^tavola', item['pres']):
#                     titolo = make_tavolarotonda(item, db)
#                     nocols = True
#             tech = ""
#             if 'TECH' in item and item['TECH'] == 'X':
#                 tech = " <img width=50 src='/images/icon/tech.svg' alt='tech'/>"
#             ora = '<a name="{label}"></a>{Ora}|{Durata}|{xtitolo}{tech}'.format(
#                 xtitolo=titolo, tech=tech,
#                 **item
#             )
#             di = ""
#             if not nocols:
#                 if 'pres' in item:
#                     pres = item['pres']
#                     if pres not in db:
#                         continue
#                     di = "|" + make_authors(item, db)
#             str_out_x += ora + di + "\n"
#         str_out.append(str_out_x)
#     if len(str_out) < 4:
#         str_out.append('')
#     dictionary = dict(zip(('VENERDI_MATTINA', 'VENERDI_POMERIGGIO', 'SABATO_MATTINA', 'SABATO_POMERIGGIO'),
#                           str_out))
#     write_out(PATH, 'programma.md', **dictionary)


def main():
    # SPREADSHEET_ID = '1ytHRQXyesPblgGe652OZLtaoGWzaaM0x8w93BN72uQM'
    SPREADSHEET_ID = '1lBx6vQW3tIB3ZsV6E_vI9hnhTCb0xE0ICg_TUBB2EVM'
    service = setup_sheet_work(SPREADSHEET_ID)

    db = read_db(service, SPREADSHEET_ID, 'Relatori!A2:S50')
    dictionary, db, pr = read_programma_db(service,
                                       SPREADSHEET_ID,
                                       db, SESSIONI)
    write_out(PATH, 'programma.md', **dictionary)

    make_speakers(service, SPREADSHEET_ID, db)
    make_interventi(service,SPREADSHEET_ID,db, pr)


if __name__ == '__main__':
    import plac
    plac.call(main)
