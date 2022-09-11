
from app import db
from app import app
import json
from urllib import parse

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    subcategory = db.Column(db.String)
    description = db.Column(db.String)
    weight = db.Column(db.Float)
    base_price = db.Column(db.Float)
    options = db.Column(db.String)
    field_selection = db.Column(db.String)
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
    picture = db.relationship('Photo', backref='coffe',
                            lazy='dynamic', cascade="all, delete, delete-orphan")

    def toDict(self):
        myDict = {}
        myDict['id'] = self.id
        myDict['name'] = self.name
        myDict['category'] = self.category
        myDict['subcategory'] = self.subcategory
        myDict['description'] = self.description
        myDict['weight'] = self.weight
        myDict['base_price'] = self.base_price
        myDict['options'] =eval(self.options)
        myDict['field_selection'] = eval(self.field_selection)
        myDict['picture'] = app.config['MEDIA_SERVER_ADDRESS']+'/'+str(self.picture.first().filename)
        return myDict
