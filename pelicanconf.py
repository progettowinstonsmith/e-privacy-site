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
EPRIVACY_N = 'XXXVII'
SESSIONI = '1M,1P,2M'.split(',')
ORGANIZZATORI = ['calamari', 'giorio', 'somma', 'berto', 'priolo', 'smith']
EVENT_PATH = 'content/2025/winter/'
YEAR = u'2025'
EDITION = 'winter'
SITENAME = u'e-privacy 2025 winter: Misurare l’Umano? Dal Vitruviano all’Algoritmo'
IMAGE='e-privacy-XXXVII.jpeg'  
PROPOSALS_OPEN = True

COUNTDOWN = False
EVENT_TIME = '2025/10/23 10:00'

# Queste variabili vengono passata a submit-propostatalk.py
SUBMIT_SETTINGS = {
    'STATIC_RECIPIENTS': [
        'segreteria@winstonsmith.org',
        'exedre@winstonsmith.org',
        'marcoc@marcoc.it'
    ],
    'SENDER_EMAIL':       'segreteria@winstonsmith.org',
    'ORG_PATH':           '/home/pws/data/proposte.org',
    'CSV_PATH':           '/home/pws/data/contacts.csv',
    'REDIRECT_URL':  '/grazie-della-proposta.html'
}

# Submit slides configuration
SLIDES_SUBMITTERS = [
    ('calamari', 'Fabio Pietrosanti (Calamari)'),
    ('giorio', 'Andrea Giorio'),
    ('somma', 'Sandro Somma'),
    ('berto', 'Stefano Berto'),
    ('priolo', 'Giovanni Priolo'),
    ('smith', 'Winston Smith'),
]

SLIDES_SETTINGS = {
    'STATIC_RECIPIENTS': [
        'segreteria@winstonsmith.org',
    ],
    'SENDER_EMAIL': 'segreteria@winstonsmith.org',
    'STORAGE_PATH': '/home/pws/data/inbound',
    'PASSWORD': 'JULIA',
    'REDIRECT_URL': '/grazie-consegna-slides.html',
    'MAX_INLINE_SIZE': 1024 * 1024 * 1024,  # 1 GiB
}

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
JINJA_GLOBALS = {
    'SLIDES_SUBMITTERS': SLIDES_SUBMITTERS,
    'SLIDES_SETTINGS': SLIDES_SETTINGS,
}

AUTHOR = u'Winston Smith'
SITESUBTITLE = u'<br/><br/><br/><i>"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli."</i> - V (da John Basil Barnhill) '
SITEURL = ''
#SITEURL = 'https://e-privacy.winstonsmith.org'
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


# DIRECT_TEMPLATES = ['index', 'archives']

DELETE_OUTPUT_DIRECTORY = True



THIS = (
#     ('Il programma', f'/e-privacy-{EPRIVACY_N}-programma.html'),
#     ('Gli interventi', f'/e-privacy-{EPRIVACY_N}-interventi.html'),
#     ('I relatori', f'/e-privacy-{EPRIVACY_N}-relatori.html'),
#     ('Iscriviti', 'https://lists.xed.it/ep2019w-registration-form'),
#     ('Call for Paper', f'/e-privacy-{EPRIVACY_N}-cfp.html'),
#     ('Call for Paper', f'http://e-privacy.winstonsmith.org/e-privacy-XXXVII-proposta.html'),   ###### ATTENZIONE QUI
     ('Proposta Talk', f'/e-privacy-proposta-talk.html'),  
#     ('Proposta Talk', f'/e-privacy-{EPRIVACY_N}-proposta.html'),
#     ('Call for Sponsor', f'/e-privacy-{EPRIVACY_N}-cfs.html'),
#     ('FAQ per i relatori', f'/e-privacy-{EPRIVACY_N}-faq-relatori.html'),
#     ('Slides', f'/consegna-slides.html'),
     ('Come arrivare', f'/e-privacy-{EPRIVACY_N}-come-arrivare.html'),
     ('Mappa delle edizioni', '/mappa-edizioni-e-privacy.html'),
     ('Donazioni', '/donazioni-e-privacy.html'),
     ('Collabora', '/collabora.html'),
     ('Contatti', '/contatti.html'),
     ('Consegna Slides', '/consegna-slides.html'),
)

ISCRIVITI='''
<a class="linkbutton"  href="http://lists.xed.it/ep2018-registration-form">Iscriviti!</a>
'''

ALL_EDIZIONI = [
    (2002, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-I.html',
            'edition': 'I',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2003, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-II.html',
            'edition': 'II',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2004, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-III.html',
            'edition': 'III',
            'location': 'Facoltà di Scienze Politiche, Aula Magna, via delle Pandette 21, 50127 Firenze',
            'lat': 43.7936710078093,
            'lon': 11.2319221893708,
        },
    }),
    (2005, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-IV.html',
            'edition': 'IV',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2006, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-V.html',
            'edition': 'V',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2007, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-VI.html',
            'edition': 'VI',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2008, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-VII.html',
            'edition': 'VII',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2009, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-VIII.html',
            'edition': 'VIII',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.25617,
        },
    }),
    (2010, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-IX.html',
            'edition': 'IX',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.256174,
        },
    }),
    (2011, {
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-X.html',
            'edition': 'X',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.256174,
        },
    }),
    (2012, {
        'winter': {
            'city': 'Torino',
            'link': '/e-privacy-XII.html',
            'edition': 'XII',
            'location': 'Politecnico di Torino, Corso Duca degli Abruzzi, 24, 10129 Torino TO',
            'lat': 45.0626206827201,
            'lon': 7.66226743224073,
        },
        'spring': {
            'city': 'Milano',
            'link': '/e-privacy-XI.html',
            'edition': 'XI',
            'location': 'Università degli Studi, Via Festa del Perdono, 7, 20122 Milano MI',
            'lat': 45.46012,
            'lon': 9.19381,
        },
    }),
    (2013, {
        'winter': {
            'city': 'Milano',
            'link': '/e-privacy-XIV.html',
            'edition': 'XIV',
            'location': 'Università Bocconi, ASK Research Center, P.za Angelo Sraffa, 13, 20136 Milano MI',
            'lat': 45.44926,
            'lon': 9.18763,
        },
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-XIII.html',
            'edition': 'XIII',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.256174,
        },
    }),
    (2014, {
        'winter': {
            'city': 'Cagliari',
            'link': '/e-privacy-XVI.html',
            'edition': 'XVI',
            'location': 'Mediateca del Mediterraneo, Via Goffredo Mameli, 164, 09123 Cagliari CA',
            'lat': 39.2215273,
            'lon': 9.1045885,
        },
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-XV.html',
            'edition': 'XV',
            'location': 'Palazzo Vecchio, P.za della Signoria, 50122 Firenze FI',
            'lat': 43.76957,
            'lon': 11.256174,
        },
    }),
    (2015, {
        'winter': {
            'city': 'Cagliari',
            'link': '/e-privacy-XVIII.html ',
            'edition': 'XVIII ',
            'location': 'Mediateca del Mediterraneo, Via Goffredo Mameli, 164, 09123 Cagliari CA',
            'lat': 39.2215273,
            'lon': 9.1045885,
        },
        'spring': {
            'city': 'Roma',
            'link': '/e-privacy-XVII.html',
            'edition': 'XVII',
            'location': 'Camera dei Deputati, Via di Campo Marzio, 78, 00186 Roma RM',
            'lat': 41.9016883770125,
            'lon': 12.477077708666,
        },
    }),
    (2016, {
        'winter': {
            'city': 'Roma',
            'link': '/e-privacy-XX.html',
            'edition': 'XX',
            'location': 'Campidoglio, Piazza del Campidoglio, 00186 Roma RM',
            'lat': 41.8935153767401,
            'lon': 12.4827607433228,
        },
        'spring': {
            'city': 'Pisa',
            'link': '/e-privacy-XIX.html',
            'edition': 'XIX',
            'location': 'Università degli Studi di Pisa, Via Giacomo Matteotti, 11, 56124 Pisa PI',
            'lat': 43.7107318754532,
            'lon': 10.4119962664637,
        },
        'extra': {
            'city': 'Udine',
            'link': '/e-privacy-3.1416.html',
            'edition': '3.1416',
            'location': 'Sala dell\'Economia Camera di Commercio di Udine, Piazza Girolamo Venerio, 7, 33100 Udine UD',
            'lat': 46.0611921424782,
            'lon': 13.236749837799,
        },
    }),
    (2017, {
        'winter': {
            'city': 'Venezia',
            'link': '/e-privacy-XXII.html',
            'edition': 'XXII',
            'location': 'Tribunale di Rialto, San Polo, 119, 30100 Venezia VE',
            'lat': 45.4388988,
            'lon': 12.3352285,
        },
        'spring': {
            'city': 'Lucca',
            'link': '/e-privacy-XXI.html',
            'edition': 'XXI',
            'location': 'Real Collegio, Piazza del Collegio, 13, 55100 Lucca LU',
            'lat': 43.8462411,
            'lon': 10.50392252,
        },
    }),
    (2018, {
        'winter': {
            'city': 'Roma',
            'link': '/e-privacy-XXIV.html',
            'edition': 'XXIV',
            'location': 'Campidoglio, Piazza del Campidoglio, 00186 Roma RM',
            'lat': 41.8935153767401,
            'lon': 12.4827607433228,
        },
        'spring': {
            'city': 'Bologna',
            'link': '/e-privacy-XXIII.html',
            'edition': 'XXIII',
            'location': 'Biblioteca Salaborsa, Piazza Nettuno 3, 40124 Bologna ',
            'lat': 44.4936714,
            'lon': 11.3430347,
        },
    }),
    (2019, {
        'winter': {
            'city': 'Bari',
            'link': '/e-privacy-XXVI.html',
            'edition': 'XXVI',
            'location': 'Ordine Avvocati di Bari, Piazza Enrico de Nicola, 1, 70123 Bari BA',
            'lat': 41.12352027474724,
            'lon': 16.85657165279148,
        },
        'spring': {
            'city': 'Torino',
            'link': '/e-privacy-XXV.html',
            'edition': 'XXV',
            'location': 'Politecnico di Torino, Corso Duca degli Abruzzi, 24, 10129 Forlì TO',
            'lat': 45.0626499683941,
            'lon': 7.66233776656111,
        },
    }),
    (2020, {
        'winter': {
            'city': 'covid',
            'link': '/e-privacy-XXVIII.html',
            'edition': 'XXVIII',
            'location': 'http://127.0.0.1',
            'lat': 43.7722395941173,
            'lon': 11.2506047028547,
        },
        'spring': {
            'city': 'covid',
            'link': '/e-privacy-XXVII.html',
            'edition': 'XXVII',
            'location': 'http://127.0.0.1',
            'lat': 43.7722395941173,
            'lon': 11.2506047028547,
        },
    }),
    (2021, {
        'winter': {
            'city': 'covid',
            'link': '/e-privacy-29e3quarti.html',
            'edition': '29e3quarti',
            'location': 'http://127.0.0.1',
            'lat': 43.7722395941173,
            'lon': 11.2506047028547,
        },
        'spring': {
            'city': 'covid',
            'link': '/e-privacy-XXIX.html',
            'edition': 'XXIX',
            'location': 'http://127.0.0.1',
            'lat': 43.7722395941173,
            'lon': 11.2506047028547,
        },
    }),
    (2022, {
        'winter': {
            'city': 'Roma',
            'link': '/e-privacy-XXXI.html',
            'edition': 'XXXI',
            'location': 'Università degli Studi Roma Tre, in via Ostiense, 163 Roma',
            'lat': 41.8625984138748,
            'lon': 12.4797359137282,
        },
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-XXX.html',
            'edition': 'XXX',
            'location': 'Sala Multimediale Infopoint,Piazza della Stazione, 4, 50123 Firenze FI',
            'lat': 43.7754177098538,
            'lon': 11.2490475524806,
        },
    }),
    (2023, {
        'winter': {
            'city': 'Pisa',
            'link': '/e-privacy-XXXIII.html',
            'edition': 'XXXIII',
            'location': 'Ordine degli Ingegneri di Pisa, Via Santa Caterina, 16 - 56127 Pisa',
            'lat': 43.7216798394982,
            'lon': 10.4023665664594,
        },
        'spring': {
            'city': 'Roma',
            'link': '/e-privacy-XXXII.html',
            'edition': 'XXXII',
            'location': 'Associazione Stampa Romana, Piazza della Torretta, 36, 00186 Roma RM',
            'lat': 41.9034193668435,
            'lon': 12.4774368020809,
        },
    }),
    (2024, {
        'winter': {
            'city': 'Brescia',
            'link': '/e-privacy-XXXV.html',
            'edition': 'XXXV',
            'location': 'Ordine degli Ingegneri della Provincia di Brescia, Via Cefalonia, 70, 25124 Brescia BS',
            'lat': 45.5249933866926,
            'lon': 10.2156898251627,
        },
        'spring': {
            'city': 'Firenze',
            'link': '/e-privacy-XXXIV.html',
            'edition': 'XXXIV',
            'location': 'Sala Multimediale Infopoint,Piazza della Stazione, 4, 50123 Firenze FI',
            'lat': 43.7754177098538,
            'lon': 11.2490475524806,
        },
    }),
    (2025, {
        'spring': {
            'city': 'Bari',
            'link': '/e-privacy-XXXVI.html',
            'edition': 'XXXVI',
            'location': 'Università degli Studi di Bari - Dipartimento di Giurisprudenza, Piazza Cesare Battisti, 1, 70122 Bari BA',
            'lat': 41.1202400901967,
            'lon': 16.8677728933869,
            },
       'winter': {
            'city': 'Firenze',
            'link': '/e-privacy-XXXVII.html',
            'edition': 'XXXVII',
            'location': 'Sala Multimediale Infopoint,Piazza della Stazione, 4, 50123 Firenze FI',
            'lat': 43.7754177098538,
            'lon': 11.2490475524806,
        },

            }),
            ]


EDIZIONI = []

for year, sessions in ALL_EDIZIONI:
    ed = {}
    for name, session in sessions.items():
        try:
            ed[name] = (session["city"], session["link"], session["edition"])
        except Exception as e:
            print(f"Errore a {year}, {name}: {e}")
    EDIZIONI.append((year, ed))

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


DEFAULT_PAGINATION = False

STATIC_PATHS = ['images', '.htaccess', 'extra/js', 'extra/cgi-bin']

EXTRA_PATH_METADATA = {
    'favicon.ico': {'path': 'favicon.ico'},  #
    'extra/js/eprivacy_locations.js': {'path': 'theme/js/eprivacy_locations.js'},
    'extra/cgi-bin/submit.py': {'path': 'cgi-bin/submit.py'},
    'extra/cgi-bin/submit-propostatalk.py': {'path': 'cgi-bin/submit-propostatalk.py'},
    'robots.txt': {'path': 'robots.txt'},
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['gened', 'submitter']

# Uncomment following line if you want document-relative URLs when developing 
RELATIVE_URLS = True

THEME = 'themes/eprivacy2'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'it': '%d-%m-%Y',
}

LOCALE = ('it_IT', 'it_IT.utf8')


CATEGORY_SAVE_AS = ''
CATEGORY_URL = ''
TAG_SAVE_AS = ''
TAG_URL = ''
AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''
ARCHIVES_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''
