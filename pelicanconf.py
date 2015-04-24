#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Winston Smith'
SITENAME = u'e-privacy: Scolleghiamo il Grande Fratello'
SITESUBTITLE = u'<br/><br/><br/><i>"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli."</i> - V (da John Basil Barnhill) '
SITEURL = ''

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

THIS = (
    ('Call for Paper', '/e-privacy-estate-2015-la-trasparenza-e-la-privacy.html'),
    ('Call for Sponsor',
     '/e-privacy-estate-2015-la-trasparenza-e-la-privacy-call-for-sponsorship.html'),
    ('Collabora con noi', 'mailto:eprivacy@winstonsmith.org?subject=Disponibilità a collaborare'),
)

# Blogroll
PREVS = (
    ('e-privacy 2014 winter edition', '/2014we'),
    ('e-privacy 2014 spring edition', '/2014'),
    ('e-privacy 2013 winter edition', '/2013we'),
    ('e-privacy 2013 spring edition', '/2013'),
    ('e-privacy 2012 winter edition', '/2012we'),
    ('e-privacy 2012 spring edition', '/2012'),
    ('e-privacy 2011', '/2011'),
    ('e-privacy 2010', '/2010'),
    ('e-privacy 2009', '/2009'),
    ('e-privacy 2008', '/2008'),
    ('e-privacy 2007', '/2007'),
    ('e-privacy 2006', '/2006'),
    ('e-privacy 2005', '/2005'),
    ('e-privacy 2004', '/2004'),
    ('e-privacy 2003', '/2003'),
    ('e-privacy 2002', '/2002'),
)

# Social widget
LINKS = (
    ('Progetto Winston Smith', 'http://winstonsmith.org/'),
    ('Centro HERMES', 'http://logioshermes.org/'),
#    ('Circolo dei Giuristi Telematici', 'http://www.giuristitelematici.it/'),
)

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
