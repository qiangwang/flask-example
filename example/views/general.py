# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, flash
from flask.ext.wtf import Form, TextField, TextAreaField, Required, Length

from example import db
from example.models import User

mod = Blueprint("general", __name__)

@mod.route('/')
def index():
    users = User.query.all()
    db.session.commit()

    return render_template("general/index.html", users=users)
