"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
import re
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint
from pathlib import Path

EPRIVACY_N = 'XXIII'

URL = 'e-privacy-'

PATH ='content/2018/summer/'

def mk_md_link(nome,label,sezione,num=EPRIVACY_N):
    return "[_{nome}_](e-privacy-{num}-{sezione}.html#{label})".format(
        nome=nome, num=num, label=label, sezione=sezione
    )

def mk_relatore(nome,label,num=EPRIVACY_N):
    return mk_md_link(nome,label,'relatori',num)

def mk_intervento(nome,label,num=EPRIVACY_N):
    return mk_md_link(nome,label,'interventi',num)

def format_relatori(relatori):
    md_relatori = []
    for relatore in re.split(';',relatori):
        md_relatori.append( mk_relatore(relatore) )
    return ','.join(md_relatori)




FORMATS = (
    lambda label,x: x,
    lambda label,x: re.sub(r'^00:','',x),
    
    
)

def make_authors(info,rdb):
    if 'pres' not in info:
        return ""
    pres = info['pres'] 
    if pres in rdb:
        record = rdb[pres]
    else:
        return ""
    org = ""
    if 'Organizzazione' in record and len(record['Organizzazione'])>0:
        org = "({Organizzazione})".format(**record)
    di = "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome} {org}</a>".format(
        num=EPRIVACY_N,
        org=org,
        **record)
    if 'altri' in info:
        altri = list(map(lambda x: x.strip(), re.split(',',info['altri'])))
        di += ", " + ", ".join(map(lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome} {org}</a>".format(
            num=EPRIVACY_N,
            **rdb[x],
            org = ("("+rdb[x]['Organizzazione']+")") if 'Organizzazione' in rdb[x] and len(rdb[x]['Organizzazione'])>0 else '',),
                                   altri))
        di = re.sub(r'(.*), ([^.]*)', '\\1 e \\2', di)
    return di


def read_db(service,id,range,HEADERS = ("label","cron","Cognome","Nome","Organizzazione","Indirizzo","Email","telefono","Durata","Argomento","Titolo","Autori","Descrizione","Bio","Consenso_pubblicazione","Consenso_registrazioni","Email2","Note",)):
    result = service.spreadsheets().values().get(spreadsheetId=id,
                                                 range=range).execute()
    values = result.get('values', [])
    infos = {}
    if not values:
        print('No data found.')
    else:
        for row in values:
            if len(row[0]):
                info = dict(zip(HEADERS,row))
                info['label']=info['label'].lower()
                if 'pres' in info:
                    info['pres']=info['pres'].lower()
                if 'altri' in info:
                    info['altri']=info['altri'].lower()
                infos[info['label'].lower()]=info
    return infos

def read_programma_db(service,id, rdb):
    Giorni = ('Venerdì','Sabato')
    models = []
    db = {}

    for J,Giorno in enumerate(Giorni):
        for K,Range in enumerate((Giorno+'!A2:I18', Giorno+'!A20:I30')):
            prog = read_db(service,id,Range,HEADERS=('label','Giorno','Ora','Durata','TECH','Titolo','Autore','pres','altri'))            
            db["{}.{}".format(J,K)]=prog
            for info in prog.values():
                if 'pres' in info and info['pres'] in rdb:
                    rdb[info['pres']]['talk'] = info
    return db,rdb


def write_out(path,fname,**kw):
    templ = (Path(path) / (fname+'.template')).read_text(encoding='utf-8')
    output = templ.format(**kw)
    (Path(path) / fname).write_text(output)


def setup_sheet_work(SPREADSHEET_ID):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service

def make_relatori(service,id,db,pr):
    relatori = {}
    for key,item in db.items():
        rkey = item['Cognome'].capitalize()
        if rkey in ('Somma', 'Calamari'):
            continue
        if 'Bio' in item:
            org = ""
            if 'Organizzazione' in item and len(item['Organizzazione'])>0:
                org = "(" + item['Organizzazione'] + ")"
            if item['Titolo'] in db:
                item['talk'] = db[item['Titolo']]['talk']
            bio = '#### <a name="{label}"></a> {Nome} {Cognome} {org} <a href="/e-privacy-{num}-programma.html#{intervento}">⇧</a>\n\n{Bio}\n'.format(num=EPRIVACY_N,org=org,intervento=item['talk']['label'],**item)
            if 'talk' in item:
                titolo = item['Titolo']
                con = ""
                if titolo in db:
                    titolo = db[titolo]['Titolo']
                if 'altri' in item['talk']:
                    label = item['label']
                    if 'altri' in item['talk']:
                        altri = list(map(lambda x: x.strip(), re.split(',',item['talk']['altri'])))
                        altri.append(item['talk']['pres'])
                        if label in altri:
                            altri.remove(label)
                        con = ", ".join(map(lambda x: "<a href=\"/e-privacy-{num}-relatori.html#{label}\">{Nome} {Cognome}</a>".format(num=EPRIVACY_N,**db[x.strip()]),altri))
                        con = " con " + re.sub(r'(.*), ([^.]*)', '\\1 e \\2', con)
                bio += "\nAd e-privacy " +  EPRIVACY_N + " presenta <b><a href=\"e-privacy-{num}-interventi.html#{label}\">".format(num=EPRIVACY_N,label=item['talk']['pres']) + titolo + "</a></b> alle <a href=\"/e-privacy-{num}-programma.html#{label}\">".format(num=EPRIVACY_N,label=item['talk']['label']) + item['talk']['Ora'] + " di " + item['talk']['Giorno'] + "</a>" +  con + "."
            bio += '\n\n'
            relatori[rkey]=bio
    str_out = ""
    for relatore in sorted(relatori.values()):
        str_out += relatore + "\n"
    write_out(PATH, 'speakers.md', RELATORI=str_out)


def make_interventi(service,id,db,pr):
    str_out = ""

    for day in pr.values():
        for key,item in day.items():
            if 'pres' in item:
                pres = item['pres']
                if pres in db:
                    xdb = db[pres]
                    if 'Descrizione' in xdb:
                        autori = make_authors(item,db)
                        info = '#### <a name="{label}"></a> {Titolo} <a href="/e-privacy-{num}-programma.html#{intervento}">⇧</a>\n**<a href="e-privacy-{num}-relatori.html#{label}">{autori}</a>**  \n\n{Descrizione}\n\n\n'.format(
                            num=EPRIVACY_N,
                            autori=autori,
                            intervento=item['label'],
                            **xdb)
                        str_out += info + "\n"
    write_out(PATH, 'interventi.md', INTERVENTI=str_out)

def make_tavolarotonda(item,db):
    pers = item['pres']
    record = db[pers]
    aList = re.split(r' *, *', record['Autori'])
    modera = aList.pop(0)
    modera = "Modera: " + make_person(modera, db)
    partecipa = "Partecipa: " + make_persons(aList,db)
    return "Tavola Rotonda: " + mk_intervento(record['Titolo'],pers) + "<br/>" + modera + "<br/>" + partecipa 

def make_person(label,db):
    return make_authors(
        { 'pres': label, 'label': label }, db ) 

def make_persons(aList,db):
    try:
        first = aList.pop(0)
        return make_authors(
            { 'pres': label, 'label': label, 'altri': ','.join(aList) }, db ) 
    except IndexError:
        return ""


def make_programma(service,id,db,pr):
    str_out = []
    for day in pr.values():
        str_out_x = ""
        for key,item in day.items():
            item['Durata']=re.sub('^00:','',item['Durata'])
            nocols = False
            titolo = item['Titolo']            
            if titolo[0]=='*':
                nocols = True
                titolo = titolo[1:]
            if 'pres' in item:
                titolo = "<a href='/e-privacy-{num}-interventi.html#{label}'>{titolo}</a>".format(
                    num = EPRIVACY_N,
                    label = item['pres'],
                    titolo = titolo,
                )
                if re.match(r'^tavola',item['pres']):
                    titolo = make_tavolarotonda(item,db)
                    nocols = True
            ora = '<a name="{label}"></a>{Ora}|{Durata}|{xtitolo}'.format(
                xtitolo = titolo,
                **item
            )
            di = ""
            if not nocols:
                if 'pres' in item:               
                    pres = item['pres']                    
                    if pres not in db:
                        continue
                    di = "|" + make_authors(item,db)
            str_out_x += ora + di + "\n"
        str_out.append(str_out_x)
    if len(str_out)<4: 
        str_out.append('')
    dictionary = dict(zip(('VENERDI_MATTINA','VENERDI_POMERIGGIO','SABATO_MATTINA','SABATO_POMERIGGIO'),
                     str_out))        
    write_out(PATH, 'programma.md', **dictionary)



def main():
    SPREADSHEET_ID = '1ytHRQXyesPblgGe652OZLtaoGWzaaM0x8w93BN72uQM'
    service = setup_sheet_work(SPREADSHEET_ID)

    db = read_db(service,SPREADSHEET_ID,'Relatori!A2:R50')
    pr,db = read_programma_db(service,SPREADSHEET_ID,db)

    make_relatori(service,SPREADSHEET_ID,db,pr)
    make_interventi(service,SPREADSHEET_ID,db,pr)
    make_programma(service,SPREADSHEET_ID,db,pr)


if __name__ == '__main__':
    import plac; plac.call(main)
