# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kmoragas'
SITENAME = u'Kmoragas'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Costa_Rica'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('TEC-Alajuela', 'http://tec.siua.ac.cr'),
         ('TEC', 'http://www.tec.ac.cr'),
         ('AccessNow', 'http://www.accessnow.org'),
         ('Jaquerespeis', 'http://www.jaquerespeis.org'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/kmoragas'),)

DEFAULT_PAGINATION = 10

#DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Inicio', '/'),
    ('P#7@ Unix', '/category/p7-unix.html'),
    ('Contacto', '/pages/contacto.html'),
    ('Archivo', '/archives.html'),
)

STATIC_PATHS = ['images', 'pdfs', 'blog']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/notmyidea"
