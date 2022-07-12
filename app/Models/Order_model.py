
from pkg_resources import require
from app import db


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    #id_payment = db.Column(db.Integer)
    #required_datetime = db.Column(db.String)
    #positions = db.Column(db.String)
    #on_place = db.Column(db.Boolean)
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
