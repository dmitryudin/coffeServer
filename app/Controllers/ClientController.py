import json
from app import app
from app.Controllers.security import generateToken
from app.Models.Client_model import Client
import qrcode
from flask import jsonify, request
from app.Security.JWT import Auth
from app.Security.JWT import Auth_model
from app import db
from flask_cors import cross_origin
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token, jwt_required, get_jwt_identity)

@app.route('/controllers/client', methods=['POST'])
@cross_origin()
def create_client():
    recvData = json.loads(request.get_data().decode('utf-8'))
    if (Auth.Auth.query.filter_by(login=recvData['phone']).first() != None):
        return jsonify({"status": "user exist"}), 409
    client = Client(firstName=recvData['name'], phone=recvData['phone'],
                                 email=recvData['email'], passwordHash=Auth.generate_password_hash(recvData['password']))
    client.is_blocked = False
    client.bonuses = 0.0
    db.session.add(client)
    db.session.commit()
    db.session.refresh(client)
    Auth.create_user(login=recvData['phone'], password=recvData['password'],
                     role=recvData['role'], real_id=client.id)
    return jsonify({"status": "ok"}), 201
    pass
    


@app.route('/controllers/client', methods=['GET'])
@jwt_required()
def get_client():
    
    user_id = Auth.Auth.query.get(get_jwt_identity()).real_id
    client = Client.query.get(user_id)
    if client == None: return{},404
    return jsonify(client.toJson())


@app.route('/controllers/client_bonuses', methods=['GET'])
def get_client_bonuses():
    user_id = request.args['user_id']
    client = Client.query.get(user_id)
    if client == None: return{},404
    return jsonify({"bonuses":client.bonuses})

@app.route('/controllers/client_bonuses', methods=['POST'])
def accrual_client_bonuses():
    data = json.loads(request.get_data().decode('utf-8'))
    user_id = data['user_id']
    client = Client.query.get(user_id)
    if client == None: return{},404
    client.bonuses += data['bonuses']
    print('user id', user_id, 'bonuses', data['bonuses'])
    db.session.add(client)
    db.session.commit()
    return jsonify({"bonuses":client.bonuses})


@app.route('/controllers/client_bonuses', methods=['DELETE'])
def debiting_client_bonuses():
    data = json.loads(request.get_data().decode('utf-8'))
    user_id = data['user_id']
    client = Client.query.get(user_id)
    if client == None: return{}, 404
    client.bonuses -= data['bonuses']
    db.session.add(client)
    db.session.commit()
    return jsonify({"bonuses":client.bonuses})


@app.route('/controllers/client', methods=['PUT'])
def update_client():
    pass


@app.route('/controllers/client', methods=['DELETE'])
def delete_client():
    pass
