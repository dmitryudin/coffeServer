from fileinput import filename
from app import app
from flask import request
import json
from app import model, db
from app import security as scr
import datetime
from flask import jsonify
import random
import string
import os


@app.route('/coffehouse/create_coffe_house')
def createCoffeHouse():
    coffeHouseObject = model.Coffehouse()
    coffeHouseObject.name = '#thefir'
    coffeHouseObject.phone = '89003334455'
    coffeHouseObject.email = 'example@mail.ru'
    coffeHouseObject.address = 'Воронеж, ул. Старых Коней, д.15а'
    db.session.add(coffeHouseObject)
    db.session.commit()
    return 'success'


@app.route('/coffehouse/get_coffe_house', methods=['GET', 'POST'])
def getCoffeHouse():
    coffeHouseObject = model.Coffehouse.query.get(1)
    data = coffeHouseObject.getData()
    resp = jsonify(data)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/coffehouse/update_coffe_house', methods=['GET', 'POST'])
def updateCoffeHouse():
    recvData = request.get_data().decode('utf-8')
    jsonData = json.loads(recvData)
    coffeHouseObject = model.Coffehouse.query.get(1)
    coffeHouseObject.name = jsonData['name']
    coffeHouseObject.phone = jsonData['phone']
    coffeHouseObject.email = jsonData['email']
    coffeHouseObject.description = jsonData['description']
    coffeHouseObject.address = jsonData['address']
    newlist = jsonData['photos']
    # TODO возможно стоит обрабатывать как можества
    oldlist = list(map(lambda x: x.filename, coffeHouseObject.photos))
    for photo in oldlist:
        if not (app.config['MEDIA_SERVER_ADDRESS']+'/'+photo in newlist):
            path = '/var/www/html/'+str(photo).split('/')[-1]
            if os.path.exists(path):
                os.remove(path)
    for photo in coffeHouseObject.photos:
        print('deleted', photo.filename)
        db.session.delete(photo)
    for photo in newlist:
        photosObject = model.Photo()
        photosObject.coffehouse_id = coffeHouseObject.id
        photosObject.filename = photo.split('/')[-1]
        db.session.add(photosObject)
        print('ph-', photosObject.filename)
    db.session.add(coffeHouseObject)
    db.session.commit()

    return ''
