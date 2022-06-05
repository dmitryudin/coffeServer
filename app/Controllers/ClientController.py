import json
from app import app
from app.Controllers.security import generateToken
from app.Models import Client_model

from flask import jsonify, request
from app.Security.JWT import Auth
from app.Security.JWT import Auth_model
from app import db
from flask_cors import cross_origin


@app.route('/controllers/client', methods=['POST'])
@cross_origin()
def create_client():
    recvData = json.loads(request.get_data().decode('utf-8'))
    if (Auth.Auth.query.filter_by(login=recvData['phone']).first() != None):
        return jsonify({"status": "user exist"}), 409
    client = Client_model.Client(firstName=recvData['name'], phone=recvData['phone'],
                                 email=recvData['email'], passwordHash=Auth.generate_password_hash(recvData['password']))

    db.session.add(client)
    db.session.commit()
    db.session.refresh(client)
    Auth.create_user(login=recvData['phone'], password=recvData['password'],
                     role=recvData['role'], real_id=client.id)
    return jsonify({"status": "ok"}), 201
    pass


@app.route('/controllers/client', methods=['GET'])
def get_client():
    pass


@app.route('/controllers/client', methods=['PUT'])
def update_client():
    pass


@app.route('/controllers/client', methods=['DELETE'])
def delete_client():
    pass
