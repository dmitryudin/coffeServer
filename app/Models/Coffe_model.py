
from app import db
from app import app
import json


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
            map(lambda x: app.config['MEDIA_SERVER_ADDRESS']+'/'+str(x.filename), self.photo)))
        return myDict
