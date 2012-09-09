# -*- coding: utf-8 -*-

from os.path import dirname,abspath

CUR_DIR = dirname(abspath(__file__))

#
# Config File
#
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 1
PRODUCTION_CONFIG = CUR_DIR + '/../website_config.py'

#
# Session | os.urandom(24)
#
SECRET_KEY = '\xb1\x88\xe7\x93\xdb\xf82\xd2\xa0}*@\xb3'

#
# DB
#
SQLALCHEMY_DATABASE_URI = 'mysql+oursql://ajk_w:ajk_w@localhost/example'

#
# Log
#
ERROR_LOG = CUR_DIR + '/../logs/flask.error.log'
ERROR_LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
