from fileinput import filename
from app import app
from flask import request
import json
from app import db
from app.Models.Coffe_house_model import Coffehouse
import datetime
from flask import jsonify
import random
import string
import os
from flask_cors import cross_origin


#@app.route('/controllers/coffehouse', methods=['POST'])
#@cross_origin()
def create_coffe_house():
    coffeHouseObject = Coffehouse()
    coffeHouseObject.name = '#thefir'
    coffeHouseObject.phone = '89003334455'
    coffeHouseObject.email = 'example@mail.ru'
    coffeHouseObject.address = 'Воронеж, ул. Старых Коней, д.15а'
    db.session.add(coffeHouseObject)
    db.session.commit()
    return '', 204


@app.route('/controllers/coffehouse', methods=['GET'])
@cross_origin()
def get_coffe_house():
    coffeHouseObject = Coffehouse.query.get(1)
    data = coffeHouseObject.toJson()
    
    return data, 200


@app.route('/controllers/coffehouse', methods=['PUT'])
@cross_origin()
def update_coffe_house():
    recvData = request.get_data().decode('utf-8')
    coffeHouseObject = Coffehouse.query.get(1)
    coffeHouseObject.fromJson(jsonString=recvData)
    return '{}', 204


@app.route('/controllers/coffehouse', methods=['DELETE'])
@cross_origin()
def delete_coffe_house():
    pass
