from app import db


class MessageQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    is_delivered = db.Column(db.Boolean)
    is_read = db.Column(db.Boolean)
    sender_id = db.Column(db.Integer)
    reciever_id = db.Column(db.Integer)
    time = db.Column(db.String)
    pass


class FriendsQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_accept = db.Column(db.Boolean)
    sender_id = db.Column(db.Integer)
    reciever_id = db.Column(db.Integer)
