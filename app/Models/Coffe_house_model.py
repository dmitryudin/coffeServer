import json
from app import db
from app import app
from flask import jsonify
import os
from app.Models.Other import Photo


class Coffehouse(db.Model):
    __tablename__ = 'coffehouse'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120))
    description = db.Column(db.String(120))
    address = db.Column(db.String(120), index=True)
    rating = db.Column(db.Float)
    photos = db.relationship('app.Models.Other.Photo', backref='coffehouse',
                             cascade="all,delete,delete-orphan", lazy='dynamic')
    orders = db.relationship(
        'app.Models.Order_model.Order', backref='coffehouse', lazy='dynamic')
    dishes = db.relationship(
        'app.Models.Dish_model.Dish', backref='coffehouse', lazy='dynamic')

    def toJson(self):
        fieldsOfClass = list(filter(lambda x: x.find('_') == -1, dir(self)))
        myDict = {}
        for el in fieldsOfClass:
            if el == 'metadata' or el == 'toJson' or el == 'fromJson' or el == 'query' or el == 'passwordHash' or el == 'registry':
                continue
            if el == 'orders' or el == 'dishes':
                continue
            if el == 'photos':
                myDict[el] = (list(
                    map(lambda x: app.config['MEDIA_SERVER_ADDRESS']+'/'+x.filename, self.photos)))
                continue
            if getattr(self, el) != None:
                myDict[el] = getattr(self, el)
            else:
                myDict[el] = ''
        return jsonify(myDict)

    def fromJson(self, jsonString):
        jsonString = json.loads(jsonString)
        self.name = jsonString['name']
        self.phone = jsonString['phone']
        self.email = jsonString['email']
        self.description = jsonString['description']
       # self.address = jsonString['address']
        newlist = jsonString['photos']
        # TODO возможно стоит обрабатывать как можества
        oldlist = list(map(lambda x: x.filename, self.photos))
        for photo in oldlist:
            if not (app.config['MEDIA_SERVER_ADDRESS']+'/'+photo in newlist):
                path = '/var/www/html/'+str(photo).split('/')[-1]
                if os.path.exists(path):
                    try:
                        os.remove(path)
                    except: pass
        for photo in self.photos:
            db.session.delete(photo)
        for photo in newlist:
            photosObject = Photo()
            photosObject.coffehouse_id = self.id
            photosObject.filename = photo.split('/')[-1]
            db.session.add(photosObject)
        db.session.add(self)
        db.session.commit()
