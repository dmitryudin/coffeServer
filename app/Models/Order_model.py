
from app import db


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
