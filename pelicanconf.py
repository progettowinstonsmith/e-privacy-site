#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

##### Mappe

# Foglio di calcolo: https://ethercalc.net/17whurbqij
# Mappa: https://umap.openstreetmap.fr/en/map/anonymous-edit/1017298:LcFDpLUxJDkPE3C8zeTixfajLac45zJn3f7M4aSPCDE


##### Configurazioni per il sync 

EDITION = 36
RELAZIONI = 'talks'
RELATORI = 'curricula'
EPRIVACY_N = 'XXXVI'
SESSIONI = '1M,1P,2M'.split(',')
ORGANIZZATORI = ['calamari', 'giorio', 'somma', 'berto', 'priolo', 'smith']
EVENT_PATH = 'content/2025/summer/'
YEAR = u'2025'
EDITION = 'summer'
SITENAME = u'e-privacy 2025 summer: La vita è tutta un dossier'
IMAGE='e-privacy-XXXVI.png'  

COUNTDOWN = False
EVENT_TIME = '2025/05/22 10:00'

#####


THIS_TITLE = f"e-privacy {YEAR} {EDITION}"


LOAD_CONTENT_CACHE = False
# CACHE_MODIFIED_METHOD = 'md5'

HOME_LINK = '/'
#HOME_LINK = 'http://localhost/'

LIVE_AT=False
# "15:00"
NOW_LIVE=False
#LIVE_URL="https://www.youtube.com/watch?v=mBLCve2YHas"
#LIVE_URL="https://www.youtube.com/watch?v=EJse8vqbkEc"
LIVE_URL="https://www.youtube.com/watch?v=m58flx5d1qI"

def split(string):
    return [x.strip() for x in string.strip().split(',')]

JINJA_FILTERS = {'split': split}

AUTHOR = u'Winston Smith'
SITESUBTITLE = u'<br/><br/><br/><i>"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli."</i> - V (da John Basil Barnhill) '
#SITEURL = ''
SITEURL = 'https://e-privacy.winstonsmith.org'
OLDSITE = 'https://e-privacy.winstonsmith.org'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_ATOM_URL = None
# CATEGORY_FEED_ATOM_URL = None
# CATEGORY_FEED_ATOM =  'feeds/{slug}.atom.xml'
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# CATEGORY_FEED_ATOM_URL = None

DIRECT_TEMPLATES = ['index', 'archives']

DELETE_OUTPUT_DIRECTORY = True



THIS = (
     ('Il programma', f'/e-privacy-{EPRIVACY_N}-programma.html'),
     ('Gli interventi', f'/e-privacy-{EPRIVACY_N}-interventi.html'),
     ('I relatori', f'/e-privacy-{EPRIVACY_N}-relatori.html'),
#     ('Iscriviti', 'https://lists.xed.it/ep2019w-registration-form'),
     ('Call for Paper', f'/e-privacy-{EPRIVACY_N}-cfp.html'),
#     ('Proposta Talk', f'/e-privacy-{EPRIVACY_N}-proposta.html'),
#     ('Call for Sponsor', f'/e-privacy-{EPRIVACY_N}-cfs.html'),
#     ('FAQ per i relatori', f'/e-privacy-{EPRIVACY_N}-faq-relatori.html'),
#     ('Slides', f'/consegna-slides.html'),
     ('Come arrivare', f'/e-privacy-{EPRIVACY_N}-come-arrivare.html'),
     ('Mappa delle edizioni', '/mappa-edizioni-e-privacy.html'),
     ('Donazioni', '/donazioni-e-privacy.html'),
     ('Collabora', '/collabora.html'),
     ('Contatti', '/contatti.html'),
)

ISCRIVITI='''
<a class="linkbutton"  href="http://lists.xed.it/ep2018-registration-form">Iscriviti!</a>
'''
EDIZIONI = [
    (2025, {
        "spring": ("Bari", "/e-privacy-XXXVI.html", "XXXVI"),
     }),    (2024, {
        "spring": ("Firenze", "/e-privacy-XXXIV.html", "XXXIV"),
        "fall": ("Brescia", "/e-privacy-XXXV.html", "XXXV"),
    }),
    (2023, {
        "spring": ("Roma", "/e-privacy-XXXII.html", "XXXII"),
        "fall": ("Pisa", "/e-privacy-XXXIII.html", "XXXIII"),
    }),
    (2022, {
        "spring": ("Firenze", "/e-privacy-XXX.html", "XXX"),
        "fall": ("Roma", "/e-privacy-XXXI.html", "XXXI"),
    }),
    (2021, {
        "spring": ("Covid", "/e-privacy-XXIX.html", "XXIX"),
        "extra": ("Hogward", "/e-privacy-29e3quarti.html", "29¾"),
    }),
    (2020, {
        "spring": ("Covid", "/e-privacy-XXVII.html", "XXVII"),
        "fall": ("Covid", "/e-privacy-XXVIII.html", "XXVIII"),
    }),
    (2019, {
        "spring": ("Torino", "/e-privacy-XXV.html", "XXV"),
        "fall": ("Bari", "/e-privacy-XXVI.html", "XXVI"),
    }),
    (2018, {
        "spring": ("Bologna", "/e-privacy-XXIII.html", "XXIII"),
        "fall": ("Roma", "/e-privacy-XXIV.html", "XXIV"),
    }),
    (2017, {
        "spring": ("Lucca", "/e-privacy-XXI.html", "XXI"),
        "fall": ("Venezia", "/e-privacy-XXII.html", "XXII"),
    }),
    (2016, {
        "spring": ("Pisa", "/e-privacy-XIX.html", "XIX"),
        "fall": ("Roma", "/e-privacy-XX.html", "XX"),
        "extra": ("Udine", "/e-privacy-3.1416.html", "π"),
    }),
    (2015, {
        "spring": ("Roma", "/e-privacy-XVII.html", "XVII"),
        "fall": ("Cagliari", "/e-privacy-XVIII.html", "XVIII"),
    }),
    (2014, {
        "spring": ("Firenze", "/e-privacy-XV.html", "XV"),
        "fall": ("Cagliari", "/e-privacy-XVI.html", "XVI"),
    }),
    (2013, {
        "spring": ("Firenze", "/e-privacy-XIII.html", "XIII"),
        "fall": ("Milano", "/e-privacy-XIV.html", "XIV"),
    }),
    (2012, {
        "spring": ("Milano", "/e-privacy-XI.html", "XI"),
        "fall": ("Torino", "/e-privacy-XII.html", "XII"),
    }),
    (2011, {
        "spring": ("Firenze", "/e-privacy-X.html", "X"),
    }),
    (2010, {
        "spring": ("Firenze", "/e-privacy-IX.html", "IX"),
    }),
    (2009, {
        "spring": ("Firenze", "/e-privacy-VIII.html", "VIII"),
    }),
    (2008, {
        "spring": ("Firenze", "/e-privacy-VII.html", "VII"),
    }),
    (2007, {
        "spring": ("Firenze", "/e-privacy-VI.html", "VI"),
    }),
    (2006, {
        "spring": ("Firenze", "/e-privacy-V.html", "V"),
    }),
    (2005, {
        "spring": ("Firenze", "/e-privacy-IV.html", "IV"),
    }),
    (2004, {
        "spring": ("Firenze", "/e-privacy-III.html", "III"),
    }),
    (2003, {
        "spring": ("Firenze", "/e-privacy-II.html", "II"),
    }),
    (2002, {
        "spring": ("Firenze", "/e-privacy-I.html", "I"),
    }),
]

# Social widget
LINKS = (
    ('Progetto Winston Smith', 'https://pws.winstonsmith.org/'),
    ('Maillist Sikurezza.org', 'https://www.sikurezza.org/'),
    ('Circolo dei Giuristi Telematici', 'http://www.giuristitelematici.it/'),
    ('Centro HERMES', 'https://hermescenter.org/'),
    ('Cassandra Crossing', 'https://www.cassandracrossing.org/'),
    ('Aneddotica Magazine', 'https://www.aneddoticamagazine.com/it/'),
)

PARTNERS = {
    # Massimo Melica
    # Aggiunti nel 2016
    'whistleblowingsolutions': ('Whistleblowing Solutions', 'whistleblowingsolutionslogo_206x165.png', 'https://www.whistleblowingsolutions.it/'),
    'APHIM' : ('Associazione Privacy and Information Healthcare Manager', 'aphim.gif', 'http://www.apihm.it/'),
    'upmansan' : ( 'Master in Management delle Aziende Sanitarie dell’Università di Pisa', 'mansan.jpg', 'http://www.mastermansan.it/'),
    # Precedenti
    'DFA': ('Digital Forensic Alumni', 'dfa.gif', 'http://www.perfezionisti.it'),
    'DIP': ('Consulente Legale Informatico DIP Srl', 'dip.png', 'http://www.consulentelegaleinformatico.it'),
    'OPSI': ('OPSI', 'opsi.jpg', 'http://opsi.aipnet.it'),
    'PI': ('Privacy International', 'privacyinternational.gif', 'http://www.privacyinternational.org'),
    'aipnet': ('Associazione Informatici Professionisti', 'aip.jpg', 'http://www.aipnet.it'),
    'al': ('Alternativa Libera', 'al.png', 'http://www.alternativalibera.org'),
    'grusp': ('GrUSP', 'grusp.png', 'http://www.grusp.org/it/'),
    'aipsi': ('A.I.P.S.I. - Associazione Italiana Professionisti Sicurezza Informatica', 'aipsi.png', 'http://www.aipsi.org'),
    'albast': ('Alba S.T. s.r.l', 'albast.png', 'http://ww.alba.st'),
    'amadir': ('AMADIR', 'amadir.jpg', 'http://www.amadir.it'),
    'ask': ('ASK dell’Università Bocconi di Milano', 'ask.png', 'http://www.ask.unibocconi.it/wps/wcm/connect/Cdr/Centro_ASK/Home'),
    'asr': ('Associazione Stampa Romana', 'asr.jpg', 'https://www.facebook.com/pages/Associazione-Stampa-Romana/181737418510039/'),
    'assodigitale': ('Assodigitale', 'assodigitale.jpg', "https://www.assodigitale.it"),
    'assoprovider': ('AssoProvider', 'assoprovider.jpg', 'http://www.assoprovider.it'),
    'bba': ('Big Brother Awards', 'bba.png', 'http://www.bigbrotherawards.org'),
    'com_cagliari2015': ('Comune di Cagliari', 'comune-cagliari-2015.png', 'http://comune.cagliari.it/portale'),
    'cagliari': ('Comune di Cagliari', 'comune-cagliari.png', 'http://comune.cagliari.it'),
    'cambio': ('Cambio - laboratorio di ricerca sulle trasformazioni sociali', 'cambio.jpg',  'http://www.cambio.unifi.it'),
    'cgt': ('Circolo dei Giuristi Telematici', 'cgt.jpg', 'http://www.giuristitelematici.it'),
    'clusit': ('Associazione Italiana per la Sicurezza Informatica', 'clusit.jpg', 'http://www.clusit.it/'),
    'combologna': ('Comune di Bologna', 'comune-bologna.jpg', 'http://www.comune.bologna.it'),
    'combologna-cb': ('Comune di Bologna', 'comune-bologna-citybrand.png', 'http://www.comune.bologna.it'),
    'comlucca': ('Comune di Lucca', 'comlucca.jpg', 'http://www.comune.lucca.it/home'),
    'comvilca': ('Comune di Villanova Canavese','covilca.jpg','http://www.comune.villanovacanavese.to.it'),
    'csa': ('Cloud Security Alliance', 'csa.jpg', 'http://cloudsecurityalliance.it'),
    'cloudusb': ('CloudUSB', 'cloudusb.png', 'http://cloudusb.net'),
    'csig': ('Centro Studi di Informatica Giuridica', 'csig.png', 'http://www.csig.it'),
    'cutaway': ('Cutaway', 'cutaway.png', 'http://www.cutaway.it'),
    'dataconsec': ('DataConSec', 'DataConSec.jpg', 'http://www.dataconsec.com'),
    'hermes': ('Centro Studi Hermes per la Trasparenza e i Diritti Civili Digitali', 'hermes.png', 'http://hermescenter.org'),
    'fiif' : ('Fondazione Italiana per l\'Innovazione Forense','fiif.png','http://fiif.it'), # kikko
    'firenze': ('Comune di Firenze', 'comune-firenze.png', "http://www.comune.fi.it/opencms/export/sites/retecivica/comune_firenze/comune/consiglio/gruppi_consiliari.htm"),
    'firenze1': ('Comune di Firenze: Consiglio di Quartiere 1', 'logoq1.gif', "http://www.comune.fi.it/opencms/export/sites/retecivica/comune_firenze/comune/consiglio/gruppi_consiliari.htm"),
    'firenze2': ('Comune di Firenze', 'comune-firenze.png', "http://www.comune.fi.it"),
    'flug': ('Firenze Linux User Group', 'flug.png', 'http://www.firenze.linux.it'),
    'golem': ('Golem', 'golem.png', 'http://golem.linux.it'),
    'icaa': ('ICAA', 'icaa-logo_small.jpg', 'http://www.criminologia.org'),
    'ictacademy': ('ICTAcademy', 'ictacademy.jpg', 'http://www.ict-academy.it'),
    'infomedia': ("Infomedia", 'infomedia.png',  'http://www.infomedia.it'),
    'interdatnet': ('InterDatNet', 'Interdatanet_no_bg_66.png', 'http://www.interdatanet.org'),
    'isgroup': ('Information Security Group', 'isgroup.png', 'https://www.isgroup.it/it/index.html'),
    'lilik': ('Lilik', 'lilik.png', 'http://www.lilik.it'),
    'luording' : ('Ordine degli Ingegneri della Provincia di Lucca', 'lu-ording.jpg','http://www.ordineingegneri.lucca.it/'),
    'lucna' : ('CNA Lucca', 'lu-cna.png','http://www.cnalucca.it/'),
    'medialaws': ('MediaLaws', 'medialaws.png', 'http://www.medialaws.eu'),
    'metro': ('Associazione Culturale Informatica Metro Olografix', 'metro.png', 'http://www.olografix.org/'),
    'nexa': ('Centro Nexa', 'nexa.jpg', 'http://nexa.polito.it/press-kit'),
    'nextel': ('Nextel Italia S.r.l.', 'nextel.png', 'http://www.nextel.it'),
    'no1984.org': ('No1984.org', 'no1984.png', 'http://www.no1984.org'),
    'oda_cagliari': ('Ordine degli Avvocati di Cagliari','oda-cagliari.png','http://www.ordineavvocaticagliari.it'),
    'odg_sardegna': ('OdG Sardegna', 'odg-sardegna.png', 'http://odg.sardegna.it'),
    'puntoi': ('Punto Informatico', 'pi.png', 'http://www.punto-informatico.it'),
    'pws': ('Progetto Winston Smith', 'pws.png', 'http://pws.winstonsmith.org'),
    'recursiva': ('Rekursiva', 'recursiva_logo.png', 'http://www.recursiva.org'),
    'reg_sardegna': ('Regione Sardegna','regione-sardegna.png','http://regione.sardegna.it'),
    'romasemplice': ('Roma Capitale, Assessorato Roma Semplice','romasemplice.jpg','http://comune.roma.it'),
    's0ftpj': ('s0ftpj', 's0ftpj_logo.png', 'http://www.s0ftpj.org'),
    'sardegnaricerche': ('Sardegna Ricerche', 'sardegnaricerche.png', 'http://www.sardegnaricerche.it/'),
    'scpol': ('Facoltà di Scienze Politiche - Università degli Studi di Firenze', 'unifi.jpg', 'http://www.scpol.unifi.it'),
    'secure_network': ('Secure Network S.r.l.', 'secure_network.png', 'http://www.securenetwork.it'),
    'segment': ('Segment is an Italian company involved in IT security and ethical hacking','segment.png','https://www.wearesegment.com'),
    'sel': ('SEL', 'sel.jpg', 'http://www.selfirenze.org'),
    'sepel': ('SEPEL', 'sepel.png', "http://www.sepel.it"),
    'sikurezza.org': ('Sikurezza.org', 'sikurezza.png', 'http://www.sikurezza.org'),
    'tramaci': ('Tramaci', 'tramaci.png', 'http://www.tramaci.org'),
    'unica': ('Università degli Studi di Cagliari - Facolta’ di Scienze Economiche, Giuridiche e Politiche', 'unica.jpg', 'http://www.unica.it/pub/7/show.jsp?id=20415&amp;iso=-2&amp;is=7'),
    'unimifsd': ('Università di Milano - Dipartimento di scienze giuridiche "Cesare Beccaria" - Sezione di Filosofia e Sociologia del Diritto', 'unimifsd.jpg', 'http://users.unimi.it/beccaria/index.php/dipartimento/filosofia-e-sociologia-del-diritto'),
    'ush': ('USH', 'ush.jpg', 'https://www.ush.it'),
    'verdi': ('Gruppo Verde', 'verdi.jpg', 'http://verdi.it'),
    'lugvr': ('Linux User Group Verona - LugVR', 'lugv.png', 'http://www.verona.linux.it'),
    'senzabarcode': ('SenzaBarcode.it', 'senzabarcode.png', 'http://www.senzabarcode.it'),
    'radioradicale': ('Radio Radicale', 'radioradicale.png', 'http://www.radioradicale.it'),
    'lalegatoria': ('la legatoria', 'lalegatoria.jpg', 'http://www.lalegatoria.it'),
    'hackthewire': ('HackTheWire', 'logo-hackthewire.png', 'https://www.hackthewire.it'),
    'mes3hacklab': ('mes3hacklab', 'mes3hacklab.png', 'http://mes3hacklab.org'),
    'overvolt': ('overvolt', 'logo_overvolt.png', 'https://www.youtube.com/channel/UCw6ekhAtFahKr7gImCIoYwg/featured'),
    'aneddotica': ('aneddotica', 'logo_aneddotica.png', 'https://www.aneddoticamagazine.com/it/'),
    'ihc': ('Italian Hacker Camp', 'logoihc_filled.png', 'https://www.ihc.camp/'),
    'ogem': ('Ordine Giornalisti Emilia-Romagna', 'logo_ordine_giornalisti_bologna.png', 'http://odg.bo.it/'),
    'brat': ('Brat Cyber Security', 'logo_brat.png', 'https://www.bratsecurity.com/'),
    'lhb': ('Legal Hackers Bari', 'logo_lhb.jpg', 'https://www.meetup.com/it-IT/Bari-Legal-Hackers/'),
    'ordavvbari': ('Ordine Avvocati Bari', 'logo_ordine_avvocati_bari.jpg', 'http://www.ordineavvocati.bari.it/'),
    'defcons': ('Defcons', 'LogoSiteDefcons.png', 'https://defcons.uno/'),
    'lealternative': ('LeAlternative.it', 'alternative-150.png', 'http://www.lealternative.it/'),
    'hackerjournal': ('Hacker Journal', 'logo_hacker_journal.jpg', 'http://www.hackerjournal.it/'),
    'gpdp': ('Garante per la Protezione dei Dati Personali', 'gpdp_logo.jpg', 'https://www.gpdp.it/'),
    'roma3': ('Università Roma Tre - Dipartimento di Giurisprudenza', 'LogoDipartimentoGiurisprudenza.jpg', 'https://www.uniroma3.it/ateneo/dipartimenti-e-scuole/dipartimenti/giurisprudenza-009447/'),
    'masterroma3': ('Master Privacy', 'logo_master.jpg', 'https://www.masterprotezionedatipersonali.it/'),
    'ordinepisa': ('Ordine Ingegneri Pisa', 'ordine_pisa.jpg', 'https://www.ordineingegneripisa.it/'),
    'ordinefirenze': ('Ordine Ingegneri Firenze', 'ordinefilogo.png', 'https://www.ordineingegneri.fi.it/'),
    'federazionetoscana': ('Federazione Regionale Ingegneri Toscana', 'federazione_regionale_ingegneri.png', 'http://www.federazioneingegneri.toscana.it/'),
    'ordineingegneribrescia': ('Ordine Ingegneri Brescia', 'logoOIB.png', 'https://brescia.ordingegneri.it/'),
    'ministerouniversitaricerca': ('Ministero Università e Ricerca', 'logomur.jpg', 'https://www.mur.gov.it/it'),
    'onif': ('Osservatorio Nazionale Informatica Forense', 'logoONIF.png', 'https://www.onif.it/'),
    'lopez': ('UgoLopez.it', 'logoUgoLopez.png', 'https://www.ugolopez.it/'),
    'faro': ('Blue Lighthouse', 'logoFaro.ai.png', 'https://blue-lighthouse.org/'),
    'uniba': ('Università degli Studi di Bari - Aldo Moro', 'logouniba.png', 'https://www.uniba.it/it'),
}



DEFAULT_PAGINATION = 1

STATIC_PATHS = ['images', '.htaccess', 'extra/js']

EXTRA_PATH_METADATA = {
    'favicon.ico': {'path': 'favicon.ico'},  #
    'extra/js/eprivacy_locations.js': {'path': 'theme/js/eprivacy_locations.js'},
}

# Uncomment following line if you want document-relative URLs when developing 
# RELATIVE_URLS = True

THEME = 'themes/eprivacy2'


DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'it': '%d-%m-%Y',
}

LOCALE = ('it_IT', 'it_IT.utf8'
          )
