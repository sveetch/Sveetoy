# -*- coding: utf-8 -*-
"""
Production settings file for project 'project'
"""
from project.settings import *

DEBUG = False

SITE_DOMAIN = 'sveetch.github.io/Sveetoy'

# Directory where all stuff will be builded
PUBLISH_DIR = os.path.join(PROJECT_DIR, '../docs')
# Path where will be moved all the static files, usually this is a directory in
# the ``PUBLISH_DIR``
STATIC_DIR = os.path.join(PROJECT_DIR, PUBLISH_DIR, 'static')
