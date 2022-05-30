from concurrent.futures.process import _python_exit
import email
import json

from sqlalchemy import values
from app import db
from app import app
#import enum
#from app import security as scr


class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(120))
    email = db.Column(db.String(120))
    role = db.Column(db.String(120))
    realid = db.Column(db.Integer)
    passwordHash = db.Column(db.String(120))


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    passwordHash = db.Column(db.String(120))
    orders = db.relationship('Order', backref='client', lazy='dynamic')


class Coffehouse(db.Model):
    #__tablename__ = 'coffehouse'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True)
    description = db.Column(db.String(120), index=True)
    address = db.Column(db.String(120), index=True)
    rating = db.Column(db.Float)
    photos = db.relationship('Photo', backref='coffehouse',
                             cascade="all,delete,delete-orphan", lazy='dynamic')
    orders = db.relationship('Order', backref='coffehouse', lazy='dynamic')
    coffes = db.relationship('Coffe', backref='coffehouse', lazy='dynamic')

    def getData(self):
        fieldsOfClass = list(filter(lambda x: x.find('_') == -1, dir(self)))
        myDict = {}
        for el in fieldsOfClass:
            if el == 'metadata' or el == 'getData' or el == 'setData' or el == 'query' or el == 'passwordHash' or el == 'registry':
                continue
            if el == 'orders' or el == 'coffes':
                continue

            if el == 'photos':
                print(list(map(lambda x: x.filename, self.photos)))
                myDict[el] = (list(
                    map(lambda x: app.config['MEDIA_SERVER_ADDRESS']+'/'+x.filename, self.photos)))
                continue
            if getattr(self, el) != None:
                myDict[el] = getattr(self, el)
        return myDict


class Coffe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)
    volumes = db.Column(db.String)
    suppliments = db.Column(db.String)
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
    photo = db.relationship('Photo', backref='coffe',
                            lazy='dynamic', cascade="all, delete, delete-orphan")

    def toDict(self):
        myDict = {}
        myDict['id'] = self.id
        myDict['name'] = self.name
        myDict['category'] = self.category
        myDict['description'] = self.description
        myDict['volumes'] = json.loads(self.volumes.replace("'", '"'))
        myDict['suppliments'] = json.loads(self.suppliments.replace("'", '"'))
        myDict['photo'] = (list(
            map(lambda x: app.config['MEDIA_SERVER_ADDRESS']+'/'+x.filename, self.photo)))
        return myDict


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    coffe_id = db.Column(db.Integer, db.ForeignKey('coffe.id'))
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
