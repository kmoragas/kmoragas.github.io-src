# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kmoragas'
SITENAME = u'kmoragas'
SITESUBTITLE = u'blog'
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

FEED_RSS = 'rss.xml'
FEED_ALL_RSS = 'all_rss.xml'
CATEGORY_FEED_RSS = '%s/rss.xml'
FEED_MAX_ITEMS = 10

# Blogroll
LINKS = (('TEC-Alajuela', 'http://tec.siua.ac.cr'),
         ('Jaquerespeis', 'http://www.jaquerespeis.org'),
         ('AccessNow', 'http://www.accessnow.org'),
         ('TEC', 'http://www.tec.ac.cr'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/kmoragas'),
          ('GitHub', 'https://github.com/kmoragas'))

DEFAULT_PAGINATION = 10

#DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Inicio', '/'),
    ('P#7@ Unix', '/category/p7-unix.html'),
    ('Cursos', 'http://tec.siua.ac.cr/~kmoragas'),
    ('Papers', '/papers.html'),
    ('Contacto', '/contacto.html'),
    ('Etiquetas', '/tags.html'),
    ('Archivo', '/archives.html'),
)

STATIC_PATHS = ['images', 'pdfs', 'blog']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

PAGE_URL = '({slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/notmyidea"

INDEX_SAVE_AS = 'blog.html'
#INDEX_URL = 'blog/'
TWITTER_USERNAME = 'kmoragas'
