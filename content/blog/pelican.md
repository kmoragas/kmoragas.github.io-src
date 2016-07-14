Title: Pelican, travis y GitHub
date: 2016-07-13 23:23
modified: 2016-07-13 23:23
Category: P#7@ Unix
Tags: pelican, travis, github
Slug: pelican-git
Authors: kmoragas
Summary: El siguiente documento intenta aclarar cómo realizar una publicación con Pelican y GitHub-Pages. Por último se agregará la sección de como realizar esta publicación de manera automática con travis. 

El siguiente documento intenta aclarar cómo realizar una publicación con Pelican y GitHub-Pages. Por último se agregará la sección de como realizar esta publicación de manera automática con travis. 

## Instalar Pelican

En fedora, se puede usar el siguiente comando: 

```
sudo dnf install python-pelican
```

Clonar el repositorio fuente

```
git clone git@github.com:username/username.github.io-src ghpages
```

Cambiarse al directorio del sitio

```
cd ghpages
```


## Configurando Pelican

Realicemos un doble chequeo en que estemos trabajando sobre el repositorio fuente: 

```
git remote -v
```

Se debería de ver el repositorio actual `username.github.io-src`. Luego es necesario clonar la salida del repositorio como si esta fuera un submódulo. 

```
git submodule add git@github.com:username/username.github.io.git output
```


Pelican provee un comando para iniciar bastante bueno. Corrámoslo:

```
pelican-quickstart
```

El quickstart hará varias preguntas, por ejemplo: 

```
    Where do you want to create your new web site? (hit Enter)
    URL prefix: http://username.github.io
    Generate a Fabfile/Makefile: Yes (for most users)
    Auto-reload & simpleHTTP script: Yes (for most users)
    Upload mechanisms: choose No for all except Github Pages
    Is this your personal page (username.github.io)? Yes
```

Una vez creado el blog por defecto. Se recomienda utilizar la siguiente distribución:

```
content/
    blog/
        articulo1.md
    images/
    pages/
        contacto.md
    pdfs/
themes/
    notmyidea/
```


El contenido de `contacto.md` se muestra a continuación. Tómese en cuenta que las metadatos son necesarios:

```
Title: Contacto
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Contacto
Tags: contacto
Slug: contacto
Authors: kmoragas
Summary: Contacto

Este es el contenido de ejemplo
```

Además ahora es necesario realizar ciertos ajustes al `pelicanconf.py`, entre ellos es requerido alterar los MENUITEMS y eliminar las categorías+paǵinas del menú principal:

```
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kmoragas'
SITENAME = u'kmoragas'
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
LINKS = (('MY-Link', '#'),)

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
```

En este momento solo queda publicar en los dos repositorios, (recordar que el segundo repo está ligado como un subrepo en `output`):

```
git add .
git commit -a -m "Mi primer post"
git push origin master
```

Luego actualizaré este documento para incluir Travis. 

# Referencias

[1] “Make a Github Pages blog with Pelican,” Fedora Magazine, 13-Oct-2015. Available: https://fedoramagazine.org/make-github-pages-blog-with-pelican/. 

[2] “Pelican 3.6.3 — Pelican 3.6.3 documentation.” [Online]. Available: http://docs.getpelican.com/en/3.6.3/index.html. [Accessed: 13-Jul-2016].


-- tuanis
