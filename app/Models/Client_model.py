from app import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    passwordHash = db.Column(db.String(120))
    orders = db.relationship('Order', backref='client', lazy='dynamic')

    def toJson(self):
        pass

    def fromJson(self, jsonString):
        pass
