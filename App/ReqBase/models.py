from enum import unique

from sqlalchemy import PrimaryKeyConstraint
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Req(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100) , nullable=False)
    app_vendor = db.Column(db.String(100) , nullable=False)   ##Creates a Req object with the shown attributes
    req_name = db.Column(db.String(100) , nullable=False)
    arch = db.Column(db.String(5), nullable=False)
    note = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)           ##Creates a User object with the shown attributes
    first_name = db.Column(db.String(150), nullable=False)
    admin = db.Column(db.Boolean(), default=True, nullable=False)
    reqs = db.relationship('Req', backref='user')
    logs = db.relationship('Log', backref='user')           ##States a relationship with Req and Log classes


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(150), db.ForeignKey('user.email'))  ##Creates a Log object with the shown attributes
    ##first_name = db.Column(db.String(150), db.ForeignKey('user.first_name')) Created first name for log
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    post = db.Column(db.String(10000))

