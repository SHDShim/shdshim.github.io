#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'S.-H. Dan Shim'
SITENAME = 'Coding Planets'
SITEURL = 'https://shdshim.github.io'

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Research', 'https://sites.google.com/site/shdshim/'),
         ('Codes', 'https://github.com/shdshim'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
# elegant is good
THEME = './pelican-themes/elegant'
SITESUBTITLE = 'coding mineralogist and dad'
GITHUB_URL = 'https://github.com/shdshim'
LANDING_PAGE_ABOUT = {
	'title': 'Coding - from research to teaching', 
	'details': 'My name is Dan Shim. I am a professor at the School of Earth and Space exploration, Arizona State University. I study minerals and their physical properties to understand the interiors of Earth, solar-system planets, and extrasolar planets. I develop codes to conduct scientific research. I am also interested in using coding for my teaching at colleage level and having fun with my kids. I hope to be able to find ways to improve learning experiences through coding.' }
PROJECTS = [{
    'name': 'Pytheos',
    'url': 'https://github.com/shdshim/pytheos',
    'description': 'A python module for equation of state'},
    {'name': 'Peakpo',
    'url': 'https://github.com/shdshim/peakpo',
    'description': 'X-ray diffraction peak analysis'}, 
    {'name': 'Scientific research',
    'url': 'https://sites.google.com/site/shdshim/',
    'description': 'Mineral physics, Geophysics, Planetary Science'}]
SITE_LICENSE = ' '