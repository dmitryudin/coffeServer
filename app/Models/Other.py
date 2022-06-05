from app import db


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    coffe_id = db.Column(db.Integer, db.ForeignKey('coffe.id'))
    coffehouse_id = db.Column(db.Integer, db.ForeignKey('coffehouse.id'))
