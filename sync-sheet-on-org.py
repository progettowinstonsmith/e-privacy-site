# coding: utf-8

"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
import re
from io import StringIO
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint,pformat
from pathlib import Path
import click
from bs4 import BeautifulSoup as bs

import logging
LOGGER = logging.getLogger("PWS")
logging.basicConfig(level=logging.INFO)

### ---------------------------------------- CONFIGURATION


RELAZIONI = 'talks'
RELATORI = 'curricula'
EPRIVACY_N = 'XXX'
SESSIONI = '1M,1P,2M,2P'.split(',')
ORGANIZZATORI = ['calamari', 'giorio', 'somma', 'berto', 'priolo', 'smith']
PATH = 'content/2022/summer/'


URL = 'e-privacy-'
PROG_FNAME = 'programma.md'
GIORNO1 = 'Giorno1'
GIORNO2 = 'Giorno2'
F_ORG = 'org'

## ---------------------------------------- FINE CONFIGURAZIONE

def program_line(*cols):
    return " | ".join(cols)

def section_open(label, kind, srange, service, _id, info, rdb):
    lines = []
    for label, record in info.items():
        try:
            people = record['pers'].strip()
            if ',' in people:
                people = re.split(r', *', people)
            else:
                people = [people, ]
            names = make_persons(people, rdb)
            durata = re.sub(r'^0(|(0:))', '', record['duration'])
            lines.append(program_line(record['begin'],
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
            people = [record['pers'], ]
            if 'altri' in record and len(record['altri'].strip())>0:
                altri = re.split(r', *', record['altri'])
                people.extend(altri)
            for person in people:
                if person in rdb:
                    rdb[person]['talk'].append( record )
                else:
                    LOGGER.error('TALK: '+person+" non nel DB")
            names = make_persons(people, rdb)
            durata = re.sub(r'^0(|(0:))', '', record['duration'])
            titolo = rdb[record['pers']]['Titolo']
            titolo = mk_intervento(titolo, record['pers'])
            lines.append(program_line(record['begin'],
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
            tavola = [record['pers'], ]
            people = []
            modera = 'tba'
            if 'altri' in record:
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
                    raise
            modera = make_persons([modera, ], rdb)
            names = make_persons(people, rdb)
            names = "Modera: "+modera+"<br/>Partecipano: "+names
            durata = re.sub(r'^0(|(0:))', '', record['duration'])
            titolo = rdb[record['pers']]['Titolo']
            titolo = "Tavola Rotonda: " + mk_intervento(titolo, record['pers'])
            lines.append(program_line(record['begin'],
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
            durata = re.sub(r'^0(|(0:))', '', record['duration'])
            lines.append(program_line(record['begin'],
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

def make_authors_roundtable(info, rdb):
    if 'altri' in info and len(info['altri'])>0:
        altri = list(map(lambda x: x.strip(), re.split(',', info['altri'])))
        pres = altri.pop(0)
        if pres in rdb:
            record = rdb[pres]
        else:
            return ""
        org = ""
        if F_ORG in record and len(record[F_ORG]) > 0:
            org = ("({"+F_ORG+"})").format(**record)
        di = "Modera: <a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome} {org}</a>".format(
            num=EPRIVACY_N,
            org=org,
            **record)
        di += "<br/>Partecipano: " + ", ".join(map(lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome} {org}</a>".format(
            num=EPRIVACY_N,
            **rdb[x],
            org=("("+rdb[x][F_ORG]+")") if F_ORG in rdb[x] and len(rdb[x][F_ORG]) > 0 else '',),
                                                   altri))
        di = re.sub(r'(.*), ([^.]+)$', '\\1 e \\2', di)
    return di


def db_get_attrs(attr,service, _id, _range, HEADERS):
    """ get an attribute from a dict of dict """
    ret = []
    lines = read_db(service, _id, _range, HEADERS)
    for values in lines.values():
        if attr in values:
            val = values[attr]
            if val:
                ret.append(val)
    return ret


def write_out(path, fname, **kw):
    LOGGER.info(f"WRITE OUT\: {fname}")
    templ_f = Path(path) / (fname+'.template')
    out_f = Path(path) / fname
    templ = templ_f.read_text(encoding='utf-8')
    output = templ.format(**kw)
    out_f.write_text(output)
    print("scrittura "+str(out_f)+" from template "+str(templ_f))
    LOGGER.info(f"WRITE OUT/: {fname}")

def write_out_debug(fname, *kw):
    LOGGER.info(f"WRITE OUT DEBUG\: {fname}")
    out_f = Path("/tmp/") / (fname + ".dbg")
    output = pformat(kw)
    out_f.write_text(output)
    print("scrittura "+str(out_f))
    LOGGER.info(f"WRITE OUT DEBUG/: {fname}")


def lay_talk(talk, item, db):
    pres = talk['pers']
    item = db[pres]
    titolo = item['Titolo']
    con = ""
    if titolo in db:
        titolo = db[titolo]['Titolo']
    if 'altri' in talk and len(talk['altri'])>0:
        label = item['label']
        altri = list(map(lambda x: x.strip(),
                         re.split(',', talk['altri'])))
        altri.append(talk['pers'])
        if label in altri:
            altri.remove(label)
        if len(altri)>0:
            con = ", ".join(map(
                lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome}</a>".format(
                    num=EPRIVACY_N, **db[x.strip()]), altri))
        con = " con " + re.sub(r'(.*), ([^.]*)', '\\1 e \\2', con)
    return talk, titolo, con

def lay_roundtable(talk, item, db):
    label = talk['pers']
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
            lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome}</a>".format(
                num=EPRIVACY_N, **db[x.strip()]), altri))
        con = " con " + re.sub(r'(.*), ([^.]*)', '\\1 e \\2', con)
    if ruolo == 'Partecipa al':
        con += " moderata da <a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome}</a>".format(num=EPRIVACY_N, **db[moderatore.strip()])
    return talk, ruolo, titolo, con

def make_roundtable(item, db):
    pers = item['author']
    aList = re.split(r' *, *', item['altri'])
    modera = aList.pop(0)
    modera = "Modera: " + make_persons(modera, db)
    partecipa = "Partecipa: " + make_persons(aList, db)
    return "Tavola Rotonda: " + mk_intervento(item['title'], pers) + "<br/>" + modera + "<br/>" + partecipa


def make_authors(info, rdb):
    if 'pers' not in info:
        return ""
    pres = info['pers']
    if pres in rdb:
        record = rdb[pres]
    else:
        return ""
    org = ""
    if F_ORG in record and len(record[F_ORG]) > 0:
        org = ("({"+F_ORG+"})").format(**record)
    di = "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome} {org}</a>".format(
        num=EPRIVACY_N,
        org=org,
        **record)
    if 'altri' in info and len(info['altri'])>0:
        altri = list(map(lambda x: x.strip(), re.split(',', info['altri'])))
        di += ", " + ", ".join(map(lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome} {org}</a>".format(
            num=EPRIVACY_N,
            **rdb[x],
            org=("("+rdb[x][F_ORG]+")") if F_ORG in rdb[x] and len(rdb[x][F_ORG]) > 0 else '',),
            altri))
        di = re.sub(r'(.*), ([^.]*)', '\\1 e \\2', di)
    return di

def make_person(label, db):
    return make_authors(
        {'pers': label,
         'label': label},
        db)

def compose_people(talk, db, all=False):
    aList = [ talk['author'], ]
    if 'altri' in talk and all:
        altri = talk['altri']
        if ',' in altri:
            aList.extend(altri.split(','))
        else:
            aList.append(altri)
    return compose_person(db['relatori'], *aList)

### ---------------------------------------- ELEMENT COMPOSITIONS

def compose_person(rdb, *people, org=True):
    LOGGER.info('COMPOSE_PERSON\: ')
    output = []
    for person in people:
        if len(person)==0:
            continue
        LOGGER.info(f'COMPOSE_PERSON=: {person}')
        person = re.sub("\d","",person)
        if person not in rdb:
            LOGGER.error(f'COMPOSE_PERSON :NO RECORD FOR: {person} {people}')
            raise "COMPOSE PERSON"
        record = rdb[person]
        o_org = ""
        if org and F_ORG in record and len(record[F_ORG])>0:
            o_org = ("({"+F_ORG+"})").format(**record)
        o_name = "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{nome} {cognome} {xorg}</a>".format(
            num=EPRIVACY_N,
            xorg=o_org,
            **record)
        output.append(o_name)
    if output:
        answer = ', '.join(output)
        answer = re.sub(r'(.*), ([^.]*)', '\\1 e \\2', answer)
        return answer

# compose_title
def compose_title(relazioni, talk):
    relazione = talk['author']
    output = None
    if relazione not in relazioni:
        LOGGER.error(f'COMPOSE_TITLE:NO RECORD FOR: {relazione}')
        raise "COMPOSE TITLE"
        return None
    record = relazioni[relazione]
    index = talk['label']
    title = record['title']
    prefix = ''
    if re.match(r'tavola rotonda',title,re.I):
        prefix = "Tavola Rotonda: "
        title = re.sub(r'^Tavola Rotonda: *','',title, re.I)
    label = record['label']
    output = f"<a name='{index}'></a>{prefix}<a href=\"/e-privacy-{EPRIVACY_N}-interventi.html#{label}\">{title}</a>"
    return output

# compose_time
# cimpose_duration

def compose_email(all_relatori, all_relazioni, db, dictionary):
    write_out(PATH,'email.md',
              RELATORI = _compose_speakers(all_relatori, db),
              INTERVENTI = _compose_interventi(all_relazioni, db),
              **dictionary)

def _compose_speakers(all_relatori, db):
    relatori = {}
    for cognome, item in sorted(all_relatori):
        rkey = item['cognome'].capitalize()
        LOGGER.info("SPEAKERS:"+cognome+"/"+rkey)
        if rkey.lower() in ORGANIZZATORI or len(rkey)==0:
            LOGGER.info("SPEAKERS:        exclude:"+rkey)
            continue
        relatori[rkey] = compose_speaker_bio(item,db)
    str_out = ""
    for label,relatore in sorted(relatori.items()):
        LOGGER.info('SPEAKERS:writeout:'+label)
        str_out += relatore + "\n"
    return str_out

def compose_speakers(all_relatori, db):
    write_out(PATH, 'speakers.md',
              RELATORI=_compose_speakers(all_relatori, db))

def compose_speaker_bio(item,db):
    label = item['label']
    if 'bio' in item:
        org = ""
        if F_ORG in item and len(item[F_ORG]) > 0:
            org = "(" + item[F_ORG] + ")"
        bio = '#### <a name="{label}"></a> {nome} {cognome} {Xorg}\n\n{bio}\n'.format(
            num=EPRIVACY_N,
            Xorg=org,
            **item )
        bio += '\n\n'
        return bio


def _compose_interventi(all_relazioni, db):
    # service, id, db, pr):
    str_out = ""
    relazioni = dict()
    for label, talk in all_relazioni:
        LOGGER.info('TALKS:writeout:'+label)
        relazioni[label] = compose_talk_info(talk, db)
    for label,relazione in sorted(relazioni.items()):
        str_out += relazione + "\n"
    return str_out

def compose_interventi(all_relazioni, db):
    write_out(PATH, 'interventi.md',
              INTERVENTI=_compose_interventi(all_relazioni, db))

def compose_talk_info(talk, db):
    label = talk['author']
    link = talk['label']
    title = talk['title']
    _title = f'#### <a name="{label}"></a> {title}'
    _up = f'<a href="/e-privacy-{EPRIVACY_N}-programma.html#{link}">⇧</a>'
    auth = [ talk['author'], ]
    _authors = "*"+compose_people(talk, db, all=True)+"*"
    desc = db['relazioni'][label]['description']
    return f'{_title}{_up}\n{_authors}\n\n{desc}\n\n'

#### ---------------------------------------- SETUP PROGRAM

def setup_title(talk, relazioni, relatori):
    return compose_title(relazioni, talk)

def setup_duration(talk, relazioni,  relatori):
    if len((talk['duration'])):
        ore, minuti  = map(int, talk['duration'].split(':'))
        if (ore != 0) or (minuti != 0):
            return str(ore*60+minuti)
    return ""

def setup_opening_author(talk, relazioni,  relatori):
    return compose_person(relatori, talk['author'])

def setup_opening_title(talk, relazioni,  relatori):
    return talk['title']

def setup_coffee_title(talk, relazioni,  relatori):
    return talk['title']

def setup_closing_author(talk, relazioni,  relatori):
    return ''

def setup_closing_title(talk, relazioni,  relatori):
    return talk['title']

def setup_welcome_author(talk, relazioni,  relatori):
    auth = talk['author']
    if auth == 'tba':
        return ''
    if auth in relatori:
        return compose_person(relatori, auth)
    return '?!?'

def setup_welcome_title(talk, relazioni,  relatori):
    return talk['title']

def setup_talk_author(talk, relazioni,  relatori):
    auth = [ talk['author'], ]
    if 'altri' in talk:
        for altro in talk['altri'].split(','):
            auth.append( altro)
    LOGGER.info(f"SETUP TALK AUTHOR=: {auth}")
    return compose_person(relatori, *auth)

def setup_roundtable_author(talk, relazioni,  relatori):
    if 'altri' in talk:
        names = talk['altri'].split(',')
        if len(names)>0:
            moderator = names.pop(0)
            partecipa = compose_person(relatori, *names)
            return "Modera: " + compose_person(relatori, moderator) + "<br/>Partecipano: " + partecipa
    return ""

def select_method_in_globals(*names):
    for name in names:
        if name in globals():
            LOGGER.info(f"SELECT METHOD=: {name}")
            return globals()[name]

def execute_method_in_globals(talk, relazioni, relatori, default, *names):
    method = select_method_in_globals(*names)
    if method:
        return method(talk, relazioni, relatori)
    return default

def setup_program_talk_items(label,talk,relazioni,relatori):
    line = []
    kind = talk['kind']
    for num, field in enumerate(('begin','duration','author', 'title')):
        LOGGER.info(f"SETUP PROGRAM\: {label} {num:02d}_{field}")
        value = execute_method_in_globals(talk,
                                          relazioni,
                                          relatori,
                                          talk[field],
                                          f'setup_{kind}_{field}',
                                          f'setup_{field}' )
        talk[f'OUT_{num:02d}_{field}'] = value
        soup = bs(value)
        talk[f'OUT_{num:02d}_{field}_txt'] = soup.get_text()
        if not(value):
            value = ""
        line.append(value)
        LOGGER.info(f"SETUP PROGRAM/: {label} {num:02d}_{field} = {value}")
    return line

def setup_program_session(info, relazioni, relatori):
    LOGGER.info(f"SETUP PROGRAM SESSION\:")
    program = info['program']
    session = []
    D_relazioni = list()
    D_relatori = list()
    for label,talk in program:
        kind = talk['kind']
        line = setup_program_talk_items(label,talk,relazioni,relatori)
        title = line.pop()
        author = line.pop()
        line.append('')
        line[-1] = "<span class='talk'>"
        if len(author) > 0:
            line[-1] += author + "<br/>"
        line[-1] += "<em>" + title +"</em>"
        line[-1] += "</span>"
        session.append('|'.join(line))
        LOGGER.info(f"SETUP PROGRAM=: {session[-1]}")
        if kind == 'roundtable':
            LOGGER.info(f"SETUP PROGRAM=: {label} ROUNDTABLE")
            relatoreX = re.sub("\d","",relatore)
            D_relatori.append((relatore, relatori[relatoreX] ))
            if 'altri' in talk:
                if len(talk['altri'])>0:
                    for altro in talk['altri'].split(','):
                        if altro in relatori:
                            D_relatori.append((altro,relatori[altro]))
        elif kind == 'talk':
            LOGGER.info(f"SETUP PROGRAM=: {label} TALK")
            relatore = talk['author']
            if relatore not in relazioni:
                LOGGER.error(f"Relatore {relatore} non in RELAZIONI")
                raise "RELATORE NON IN RELAZIONI"
            intervento = relazioni[relatore]
            D_relazioni.append((relatore, talk))
            relatoreX = re.sub("\d","",relatore)
            if relatoreX not in relazioni:
                LOGGER.error(f"Relatore {relatoreX} non in RELAZIONI")
                raise "RELATORE NON IN RELAZIONI"
            D_relatori.append((relatore, relatori[relatoreX] ))
            if 'altri' in talk:
                if len(talk['altri'])>0:
                    for altro in talk['altri'].split(','):
                        if altro in relatori:
                            D_relatori.append((altro,relatori[altro]))
                        else:
                            LOGGER.error(f"Relatore {altro} non in RELATORI")
                            raise "RELATORE NON IN RELAZIONI"
    LOGGER.info(f"SETUP PROGRAM SESSION/: {label}")
    return session, D_relazioni, D_relatori


#### ---------------------------------------- READ FUNCTIONS

def read_db(service, range, tweak_item=None, tweak_collection=None, session=None):
    values = service[range]
    infos = {}
    for jj,row in enumerate(values):
        print(jj,row)
        if jj == 0:
            HEADERS = [x.strip().lower() for x in row]
            HEADERS[0] = "_"
            continue
        if row[1][0]=="<":
            continue
        if len(row[1]):
            info = dict(zip(HEADERS, row))
            del info[""]
            del info["_"]
            info['label'] = info['label'].lower()
            if 'pers' in info:
                info['pers'] = info['pers'].lower()
            if 'altri' in info:
                info['altri'] = info['altri'].lower()
            if tweak_item:
                info = tweak_item(info)
            if session is not None:
                if 'session' in info and info['session'].lower() != session.lower():
                    continue
                LOGGER.info(f"SELECITN SESSIO {session} {info['label']}")
            if info['label'][0] != "<":
                infos[info['label'].lower()] = info
    if tweak_collection:
        infos = tweak_collection(infos)
    return infos


def tweak_relazioni(info):
    info['talk']=[]
    info['roundtable']=[]
    return info

def tweak_sessioni(info):
    LOGGER.info("LABEL:"+info['label'])
    if info['label'][-2:].lower() == 'aa':
        info['label'] = 'apertura'
        info['kind'] = 'opening'
        info['order'] = -1
    elif info['label'][-2:].lower() == 'ss':
        info['label'] = 'saluti'
        info['kind'] = 'welcome'
        info['order'] = 0
    elif info['label'][-2:].lower() == 'zz':
        info['label'] = 'chiusura'
        info['kind'] = 'closing'
        info['order'] = 100
    elif info['label'][-2:].lower() == 'pp':
        info['label'] = 'coffee'
        info['kind'] = 'coffee'
        info['order'] = 100
    else:
        order = int(info['label'][-2:])
        info['order'] = order
        info['kind'] = 'talk'
        if info['author'][:6] == 'tavola':
            info['kind'] = 'roundtable'
    return info

def tweak_sessioni_collection(info):
    # Chairman dell'apertura
    program = []
    for key, value in sorted( info.items(),
                              key=lambda x : (re.sub(r':','',x[1]['begin']))):
        program.append((key, value))
    return { 'program' :  program,
             'chairman' : info['apertura']['author'] if 'apertura' in info else "ND" }

def read_programma_db(service, _id, rdb, SESSIONI):
    variables = {}
    db = {}
    J = 0
    K = 0
    for variable, J, K, sessione, chair in SESSIONI:
        program = []
        db["{}.{}".format(J,K)] = {}
        chairman = db_get_attrs('pers',service, _id, chair, PROGRAMMA_HEADERS)
        if chairman:
            chairman = re.split(r'\s*,\*',chairman[0])
            chairman = compose_person(rdb, *chairman)
        LOGGER.info('SESSIONE '+variable)
        LOGGER.info('CHAIRMAN '+chairman)
        for label, kind, srange in sessione:
            LOGGER.info('    PARTE '+label)
            prog = read_db(service,
                           _id,
                           srange,
                           PROGRAMMA_HEADERS)
            db["{}.{}".format(J,K)].update(prog)
            func = "section_" + kind
            if func not in globals():
                raise SyntaxError('function {} '
                'not in globals()'.format(func))
            else:
                func = globals()[func]
            prglines, rdb = func(label, kind, srange,
                                 service, _id, prog,
                                 rdb)
            program.extend(prglines)
        variables[variable] = '\n'.join(program)
        variables["CHAIRMAN_" + variable]=compose_person(rdb,chairman)
    return variables, rdb, db

#### ---------------------------------------- END READ FUNCTIONS


#### ---------------------------------------- SETUP SYNC SHEET

def setup_sheet_work(fh):
    names = []
    tables = [[]]
    n = 0
    lines = [x.rstrip() for x in fh.readlines()]
    for j,line in enumerate(lines):
        if re.match(r"^\s*$",line):
            if(len(tables[-1]))==0:
                continue
            else:
                n += 1
                tables.append(list())
                continue
        m=re.match(r"^#\+NAME:(.+)$",line,re.I)
        if (m):
            names.append(m.group(1).strip().lower())
            continue
        m=re.match(r"^#.+$",line)
        if (m):
            continue
        m=re.match(r"^\|[-+]+\|$",line)
        if (m):
            continue
        m=re.match(r"^\|.+$",line)
        if not(m):
            continue
        tables[-1].append(re.split(r"\s*\|\s*",line))
    return dict(zip(names,tables))

def select_session_in_db(schedule,session, tweak_collection):
    ret = {}
    for key, value in schedule.items():
        print(key)
        if value['session'] == session:
            ret[key] = value
    if tweak_collection:
        ret = tweak_collection(ret)
    return { 'program': ret}

def dict_print(aDict):
    if isinstance(aDict,dict):
        return    ' | '.join([ f"{str(value):>10}" for value in aDict.values() ])
    return aDict

def db_info(dbname,db):
    keys = ' '.join(db.keys())
    LOGGER.info(f"DB INFO {dbname} {keys}")
    if False:
        for key, line in db.items():
            LOGGER.info(f"{key} {dict_print(line)}")

def print_schedule(db):
    sh = StringIO()
    sessioni  = [ "G"+x for x in db['sessioni']]
    for session in sessioni:
        sh.write(f"Moderator: {db[session]['chairman']}\n")
        table = []
        for label,event in db[session]['program']:
            row = []
            for num, field in enumerate(('begin','duration','author', 'title')):
                value = event[f'OUT_{num:02d}_{field}_txt']
                row.append(value)
            table.append(row)
            sh.write(f"{row[0]} {row[1]:>4} {row[2]}\n            {row[3]}\n")
    print(sh.getvalue())
@click.command()
@click.argument('input',type=click.File("r"))
@click.option('--debug/--no-debug', default=False)
@click.option('--debug-section', type=click.Choice(['db', 'program',
                                                    'relazioni','relatori']))
def main(input,debug,debug_section):
    LOGGER.info('service beginning')
    service = setup_sheet_work(input)
    LOGGER.info('service loaded')
    relatori = read_db(service, RELATORI  )
    db_info("relatori",relatori)
    relazioni = read_db(service, RELAZIONI, tweak_item = tweak_relazioni )
    db_info("relazioni",relazioni)
    relatori_senza_curriculum =  { k: "*" if k in relatori else "" for k in relazioni.keys() }
    print(",".join([f"{relatore}{curriculump}"
                    for relatore,curriculump in sorted(relatori_senza_curriculum.items())
                    if relatore not in relatori
                    ]))
    db = {'relatori': relatori, 'relazioni': relazioni , 'sessioni': SESSIONI }
    dictionary = {}
    all_relazioni = list()
    all_relatori = list()
    for session in SESSIONI:
        sess_db = read_db(service, "schedule",
                          session = session,
                          tweak_item = tweak_sessioni,
                          tweak_collection = tweak_sessioni_collection)
        label = 'G' + session
        LOGGER.info(f'session: {label} {",".join(dict(all_relatori).keys())}')
        db[label] = sess_db
        session, D_relazioni, D_relatori = setup_program_session(db[label],
                                                                 relazioni,
                                                                 relatori)
        all_relazioni.extend(D_relazioni)
        all_relatori.extend(D_relatori)
        dictionary[label] = '\n'.join(session)
        dictionary[f'{label}_CHAIRMAN'] = compose_person(relatori,sess_db['chairman'])
    db['_relazioni'] = dict(all_relazioni)
    db['_relatori'] = dict(all_relatori)
    if debug:
        write_out_debug("db",db)
    if debug and debug_section=='db':
        pprint(db)
        return
    LOGGER.info('db loaded')
    if debug and debug_section=='relatori':
        pprint(all_relatori)
        return
    if debug and debug_section=='relazioni':
        pprint(all_relazioni)
        return
    write_out(PATH, PROG_FNAME , **dictionary)
    compose_speakers(all_relatori, db)
    compose_interventi(all_relazioni, db)
    compose_email(all_relatori, all_relazioni, db, dictionary)
    print_schedule(db)

if __name__ == '__main__':
    main()
