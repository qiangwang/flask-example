# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

#
# Configs
#
app.config.from_object("website_config")

try:
    app.config.from_pyfile(app.config['PRODUCTION_CONFIG'], silent=False)
    print '[SUCCESS] load config file: ' + app.config['PRODUCTION_CONFIG']
except:
    print '[ERROR] load config file:' + app.config['PRODUCTION_CONFIG']

#
# DB
#
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


#
# Blueprints
#
from example.views import general

app.register_blueprint(general.mod)

#
# Handlers
#
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.teardown_request
def shutdown_session(response):
    db.session.remove()
    return response

#
# Context
#
from example import getter

@app.context_processor
def inject_getter():
    return dict(getter=getter)

#
# Log
#
if not app.debug:
    import logging
    ft = logging.Formatter(app.config['ERROR_LOG_FORMAT'])
    
    fh = logging.FileHandler(app.config['ERROR_LOG'])
    fh.setFormatter(ft)
    fh.setLevel(logging.WARNING)
    app.logger.addHandler(fh)
