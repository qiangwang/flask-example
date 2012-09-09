# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import *

from example import db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    create_time = Column(DateTime)

    def __init__(self, name):
        self.name = name
        self.create_time = datetime.now()

    def __repr__(self):
        return '<User %r>' % self.name
