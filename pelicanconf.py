#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False


def split(string):
    return [x.strip() for x in string.strip().split(',')]

JINJA_FILTERS = {'split': split}

AUTHOR = u'Winston Smith'
SITENAME = u'e-privacy 2015: La trasparenza e la privacy'
SITESUBTITLE = u'<br/><br/><br/><i>"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli."</i> - V (da John Basil Barnhill) '
SITEURL = ''
OLDSITE = 'http://e-privacy.winstonsmith.org'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'

YEAR = u'2015'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', 'archives']

THIS = (
    ('Call for Paper', '/e-privacy-XVI.html'),
    ('Call for Sponsor',
     '/e-privacy-XVI-cfs.html'),
    ('Collabora con noi', 'mailto:eprivacy@winstonsmith.org?subject=Disponibilità a collaborare'),
)

# Blogroll
PREVS = (
    ('e-privacy 2014 winter edition', '/e-privacy-XVI.html'),
    ('e-privacy 2014 spring edition', '/e-privacy-XV.html'),
    ('e-privacy 2013 winter edition', '/e-privacy-XIV.html'),
    ('e-privacy 2013 spring edition', '/e-privacy-XIII.html'),
    ('e-privacy 2012 winter edition', '/e-privacy-XII.html'),
    ('e-privacy 2012 spring edition', '/e-privacy-XI.html'),
    ('e-privacy 2011', '/e-privacy-X.html'),
    ('e-privacy 2010', '/e-privacy-IX.html'),
    ('e-privacy 2009', '/e-privacy-VIII.html'),
    ('e-privacy 2008', '/e-privacy-VII.html'),
    ('e-privacy 2007', '/e-privacy-VI.html'),
    ('e-privacy 2006', '/e-privacy-V.html'),
    ('e-privacy 2005', '/e-privacy-IV.html'),
    ('e-privacy 2004', '/e-privacy-III.html'),
    ('e-privacy 2003', '/e-privacy-II.html'),
    ('e-privacy 2002', '/e-privacy-I.html'),
)

# Social widget
LINKS = (
    ('Progetto Winston Smith', 'http://pws.winstonsmith.org/'),
    ('Centro HERMES', 'http://logioshermes.org/'),
    #    ('Circolo dei Giuristi Telematici', 'http://www.giuristitelematici.it/'),
)

PARTNERS = {
    # Massimo Melica
    'DFA': ('Digital Forensic Alumni', 'dfa.gif', 'http://www.perfezionisti.it'),
    'DIP': ('Consulente Legale Informatico DIP Srl', 'dip.png', 'http://www.consulentelegaleinformatico.it'),
    'OPSI': ('OPSI', 'opsi.jpg', '(http://opsi.aipnet.it'),
    'PI': ('Privacy International', 'privacyinternational.gif', 'http: // www.privacyinternational.org'),
    'aipnet': ('Associazione Informatici Professionisti', 'aip.jpg', 'http://www.aipnet.it'),
    'aipsi': ('A.I.P.S.I. - Associazione Italiana Professionisti Sicurezza Informatica', 'aipsi.png', 'http://www.aipsi.org'),
    'albast': ('Alba S.T. s.r.l', 'albast.png', 'http://ww.alba.st'),
    'amadir': ('AMADIR', 'amadir.jpg', 'http://www.amadir.it'),
    'asr': ('Associazione Stampa Romana', 'asr.png', 'http://www.stamparomana.it/'),
    'assodigitale': ('Assodigitale', 'assodigitale.jpg', "https://www.assodigitale.it"),
    'assoprovider': ('AssoProvider', 'assoprovider.jpg', 'http: // www.assoprovider.it'),
    'bba': ('Big Brother Awards', 'bba.png', 'http://www.bigbrotherawards.org'),
    'cagliari': ('Comune di Cagliari', 'comune-cagliari.png', 'http://comune.cagliari.it/portale'),
    'cgt': ('Circolo dei Giuristi Telematici', 'cgt.gif', 'http://www.giuristitelematici.it'),
    'clusit': ('Associazione Italiana per la Sicurezza Informatica', 'clusit.jpg', 'http://www.clusit.it/'),
    'csa': ('Cloud Security Alliance', 'csa.jpg', 'http://cloudsecurityalliance.it'),
    'cloudusb': ('CloudUSB', 'cloudusb.png', 'http://cloudusb.net'),
    'csig': ('Centro Studi di Informatica Giuridica', 'csig.png', 'http://www.csig.it'),
    'cutaway': ('Cutaway', 'cutaway.png', 'http://www.cutaway.it'),
    'dataconsec': ('DataConSec', 'DataConSec.jpg', 'http://www.dataconsec.com'),
    'hermes': ('Centro Studi Hermes per la Trasparenza e i Diritti Civili Digitali', 'hermes.png', 'http://logioshermes.org'),
    'firenze': ('Comune di Firenze', 'comune-firenze.png', "http://www.comune.fi.it/opencms/export/sites/retecivica/comune_firenze/comune/consiglio/gruppi_consiliari.htm"),
    'firenze1': ('Comune di Firenze: Consiglio di Quartiere 1', 'logoq1.gif', "http://www.comune.fi.it/opencms/export/sites/retecivica/comune_firenze/comune/consiglio/gruppi_consiliari.htm"),
    'flug': ('Firenze Linux User Group', 'flug.png', 'http://flug.linux.it'),
    'golem': ('Golem', 'golem.png', 'http://golem.linux.it'),
    'icaa': ('ICAA', 'icaa-logo_small.jpg', 'http://www.criminologia.org'),
    'ictacademy': ('ICTAcademy', 'ictacademy.jpg', 'http://www.ict - academy.it'),
    'infomedia': ("Infomedia", 'infomedia.png',  'http://www.infomedia.it'),
    'interdatnet': ('InterDatNet', 'Interdatanet_no_bg_66.png', 'http://www.interdatanet.org'),
    'isgroup': ('Information Security Group', 'isgroup.png', 'http://www.isgroup.it/it/index.html'),
    'lilik': ('Lilik', 'lilik.png', 'http://www.lilik.it'),
    'metro': ('Associazione Culturale Informatica Metro Olografix', 'metro.png', 'http://www.olografix.org/'),
    'nexa': ('Centro Nexa', 'nexa.jpg', 'http://nexa.polito.it/press-kit'),
    'nextel': ('Nextel Italia S.r.l.', 'nextel.png', 'http://www.nextel.it'),
    'no1984.org': ('No1984.org', 'no1984.png', 'http://www.no1984.org'),
    'puntoi': ('Punto Informatico', 'pi.png', 'http://www.punto-informatico.it'),
    'pws': ('Progetto Winston Smith', 'pws.png', 'http://pws.winstonsmith.org'),
    'recursiva': ('Rekursiva', 'recursiva_logo.png', 'http://www.recursiva.org'),
    's0ftpj': ('s0ftpj', 's0ftpj_logo.png', 'http://www.s0ftpj.org'),
    'sardegnaricerche': ('Sardegna Ricerche', 'sardegnaricerche.png', 'http://www.sardegnaricerche.it/'),
    'secure_network': ('Secure Network S.r.l.', 'secure_network.png', 'http://www.securenetwork.it'),
    'sel': ('SEL', 'sel.jpg', 'http://www.selfirenze.org'),
    'sepel': ('Sepel', 'sepel.png', "http://www.sepel.it"),
    'sikurezza.org': ('Sikurezza.org', 'sikurezza.gif', 'http://www.sikurezza.org'),
    'tramaci': ('Tramaci', 'tramaci.png', 'http://www.tramaci.org'),
    'unica': ('Università degli Studi di Cagliari - Facolta’ di Scienze Economiche, Giuridiche e Politiche', 'unica.jpg', 'http://www.unica.it/pub/7/show.jsp?id=20415&amp;iso=-2&amp;is=7'),
    'ush': ('USH', 'ush.jpg', 'http://www.ush.it'),
    'verdi': ('Gruppo Verde', 'verdi.jpg', 'http://verdi.it'),
    'lugvr': ('Linux User Group Verona - LugVR', 'lugv.png', 'http://www.verona.linux.it'),
}

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'pdfs', 'audio']
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/eprivacy'


DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'it': '%d-%m-%Y',
}

LOCALE = ('it_IT',
          )
