from app import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    qr = db.Column(db.String(120))
    is_blocked=db.Column(db.Boolean)
    bonuses = db.Column(db.Float)
    passwordHash = db.Column(db.String(120))
    orders = db.relationship('app.Models.Order_model.Order', backref='client', lazy='dynamic',  cascade="all, delete, delete-orphan")

    def toJson(self):
        json = {}
        json['firstName'] = self.firstName
        json['email'] = self.email
        json['phone'] = self.phone
        json['is_blocked'] = self.is_blocked
        json['bonuses'] = self.bonuses
        json['id'] = self.id
        return json

    def fromJson(self, jsonString):
        pass
