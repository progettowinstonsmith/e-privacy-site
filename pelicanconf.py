#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False
# CACHE_MODIFIED_METHOD = 'md5'

EVENT_TIME = '2019/06/06 09:30'

COUNTDOWN = False

EVENTBRITE_EID="""
<div style="width:195px; text-align:center;" ><iframe  src="https://www.eventbrite.it/countdown-widget?eid=37526459651" frameborder="0" height="544" width="195" marginheight="0" marginwidth="0" scrolling="no" allowtransparency="true"></iframe><div style="font-family:Helvetica, Arial; font-size:12px; padding:10px 0 5px; margin:2px; width:195px; text-align:center;" ><a class="powered-by-eb" style="color: #ADB0B6; text-decoration: none;" target="_blank" href="http://www.eventbrite.it/">Con tecnologia Eventbrite</a></div></div>
"""

# HOME_LINK = 'http://localhost/'
HOME_LINK = '/'

def split(string):
    return [x.strip() for x in string.strip().split(',')]

JINJA_FILTERS = {'split': split}

AUTHOR = u'Winston Smith'
SITENAME = u'e-privacy 2019 summer: Nuove tecnologie di controllo'
SITESUBTITLE = u'<br/><br/><br/><i>"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli."</i> - V (da John Basil Barnhill) '
SITEURL = ''
OLDSITE = 'https://e-privacy.winstonsmith.org'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'

YEAR = u'2019'
EDITION = 'summer'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', 'archives']

DELETE_OUTPUT_DIRECTORY = True

THIS_TITLE = "EPRIVACY 2019 - SUMMER"

THIS = (
     # ('Iscriviti', 'http://lists.xed.it/ep2018w-registration-form'),
     ('Proposta Talk', '/e-privacy-XXV-proposta.html'),
     ('Call for Paper', '/e-privacy-XXV-cfp.html'),
     # ('Slides', '/e-privacy-XXIV-programma-slides.html'),
     # ('Il programma', '/e-privacy-XXIV-programma.html'),
     # ('Gli interventi', '/e-privacy-XXIV-interventi.html'),
     # ('I relatori', '/e-privacy-XXIV-relatori.html'),
     # ('Call for Sponsor', '/e-privacy-XXIV-cfs.html'),
     # ('FAQ per i relatori', '/e-privacy-XXIV-faq-relatori.html'),
     # ('Come arrivare', '/e-privacy-XXIV-come-arrivare.html'),
     ('Donazioni', '/donazioni-e-privacy.html'),
     ('Collabora', '/collabora.html'),
     ('Contatti', '/contatti-XXIV.html'),
)

ISCRIVITI='''
<a class="linkbutton"  href="http://lists.xed.it/ep2018-registration-form">Iscriviti!</a>
'''

# PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)

# Blogroll
PREVS = (
    ('mappa di tutte le edizioni', '/mappa.html'),
    ('e-privacy 2019 winter XXIV', '/e-privacy-XXIV.html'),
    ('e-privacy 2018 summer XXIII', '/e-privacy-XXIII.html'),
    ('e-privacy 2017 autumn XXII', '/e-privacy-XXII.html'),
    ('e-privacy 2017 summer XXI', '/e-privacy-XXI.html'),
    ('e-privacy 2016 autumn XX', '/e-privacy-XX.html'),
    ('e-privacy 2016 spring XIX', '/e-privacy-XIX.html'),
    ('e-privacy 2015 autumn XVIII', '/e-privacy-XVIII.html'),
    ('e-privacy 2015 spring XVII', '/e-privacy-XVII.html'),
    ('e-privacy 2014 autumn XVI', '/e-privacy-XVI.html'),
    ('e-privacy 2014 spring XV', '/e-privacy-XV.html'),
    ('e-privacy 2013 autumn XIV', '/e-privacy-XIV.html'),
    ('e-privacy 2013 spring XIII', '/e-privacy-XIII.html'),
    ('e-privacy 2012 autumn XII', '/e-privacy-XII.html'),
    ('e-privacy 2012 spring XI', '/e-privacy-XI.html'),
    ('e-privacy 2011 X', '/e-privacy-X.html'),
    ('e-privacy 2010 IX', '/e-privacy-IX.html'),
    ('e-privacy 2009 VIII', '/e-privacy-VIII.html'),
    ('e-privacy 2008 VII', '/e-privacy-VII.html'),
    ('e-privacy 2007 VI', '/e-privacy-VI.html'),
    ('e-privacy 2006 V', '/e-privacy-V.html'),
    ('e-privacy 2005 IV', '/e-privacy-IV.html'),
    ('e-privacy 2004 III', '/e-privacy-III.html'),
    ('e-privacy 2003 II', '/e-privacy-II.html'),
    ('e-privacy 2002 I', '/e-privacy-I.html'),
)

# Social widget
LINKS = (
    ('Progetto Winston Smith', 'https://pws.winstonsmith.org/'),
    ('Centro HERMES', 'http://logioshermes.org/'),
    #    ('Circolo dei Giuristi Telematici', 'http://www.giuristitelematici.it/'),
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
    'hermes': ('Centro Studi Hermes per la Trasparenza e i Diritti Civili Digitali', 'hermes.png', 'http://logioshermes.org'),
    'fiif' : ('Fondazione Italiana per l\'Innovazione Forense','fiif.png','http://fiif.it'), # kikko
    'firenze': ('Comune di Firenze', 'comune-firenze.png', "http://www.comune.fi.it/opencms/export/sites/retecivica/comune_firenze/comune/consiglio/gruppi_consiliari.htm"),
    'firenze1': ('Comune di Firenze: Consiglio di Quartiere 1', 'logoq1.gif', "http://www.comune.fi.it/opencms/export/sites/retecivica/comune_firenze/comune/consiglio/gruppi_consiliari.htm"),
    'flug': ('Firenze Linux User Group', 'flug.png', 'http://www.firenze.linux.it'),
    'golem': ('Golem', 'golem.png', 'http://golem.linux.it'),
    'icaa': ('ICAA', 'icaa-logo_small.jpg', 'http://www.criminologia.org'),
    'ictacademy': ('ICTAcademy', 'ictacademy.jpg', 'http://www.ict-academy.it'),
    'infomedia': ("Infomedia", 'infomedia.png',  'http://www.infomedia.it'),
    'interdatnet': ('InterDatNet', 'Interdatanet_no_bg_66.png', 'http://www.interdatanet.org'),
    'isgroup': ('Information Security Group', 'isgroup.png', 'http://www.isgroup.it/it/index.html'),
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
    'ush': ('USH', 'ush.jpg', 'http://www.ush.it'),
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
}



DEFAULT_PAGINATION = 1

STATIC_PATHS = ['images', 'pdfs', 'audio', '.htaccess']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/eprivacy2'


DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'it': '%d-%m-%Y',
}

LOCALE = ('it_IT',
          )
