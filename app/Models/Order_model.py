
from pkg_resources import require
from app import db
import json
from urllib import parse
from app.Models.Client_model import Client

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    id_payment = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    required_datetime = db.Column(db.String)
    #comment = db.Column(db.String)
    positions = db.Column(db.String)
    total_cost = db.Column(db.Float)
    is_active = db.Column(db.Boolean)
    is_payd_for = db.Column(db.Boolean)
    is_accepted = db.Column(db.Boolean)
    is_ready = db.Column(db.Boolean)
    is_alarmed = db.Column(db.Boolean)
    on_place = db.Column(db.Boolean)
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    def toJson(self):
        myDict = {}
        myDict['id'] = self.id
        myDict['id_payment'] = self.id_payment
        myDict['required_datetime'] = self.required_datetime
        myDict['positions'] = eval(self.positions)
        myDict['total_cost'] = self.total_cost
        myDict['is_payd_for']  =self.is_payd_for
        myDict['is_active'] = self.is_active
        myDict['is_accepted'] = self.is_accepted
        myDict['user_id'] = self.user_id
        myDict['user_phone'] =  Client.query.get(self.user_id).phone
        myDict['on_place'] = self.on_place
        myDict['is_ready'] = self.is_ready
        myDict['is_alarmed'] = self.is_alarmed
        return (myDict)
