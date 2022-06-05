import os
from app import app
from app import db
from app.Models import model
import json
from flask import request
from flask import jsonify
from app.Models.Coffe_house_model import Coffehouse
from app.Models.Coffe_model import Coffe
from app.Models.Other import Photo
from flask_cors import cross_origin


@app.route('/controller/coffes', methods=['GET'])
@cross_origin()
def get_coffes():
    ''' 
    если url в базе данных не соответсвует переданному, то
    изображение на сервере удаляется, если вместо url передаётся base64 строка,
    то создаётся новое изображение. Метод возвращает новый массив c url картинок
    '''
    #d = json.loads(request.get_data().decode('utf-8'))
    coffeHouse = Coffehouse.query.get(int(1))
    coffes = coffeHouse.coffes.all()

    data = list(map(lambda coffe: coffe.toDict(), coffes))
    data = (jsonify(data))
    # TODO нужно реализовать этот контроллер всё-таки
    return data


@app.route('/controller/coffe', methods=['POST'])
@cross_origin()
def coffe_create():
    '''
    получает на вход массив с url изображений
    если url в базе данных не соответсвует переданному, то
    изображение на сервере удаляется, если вместо url передаётся base64 строка,
    то создаётся новое изображение. Метод возвращает новый массив c url картинок
    '''
    d = json.loads(request.get_data().decode('utf-8'))
    # if d['picture'] == '' or d['name'] == '':
    if d['name'] == '':
        return {}, 500
    coffeHouse = Coffehouse.query.get(1)
    coffes = (coffeHouse.coffes)
    coffe = Coffe()
    coffe.name = d['name']
    photo = Photo()
    if d['picture']:
        photo.filename = d['picture'].split('/')[-1]
    coffe.photo = [photo]
    coffe.category = d['category']
    coffe.description = d['description']
    coffe.suppliments = str(d['properties'])
    coffe.volumes = str(d['priceOfVolume'])
    coffes.append(coffe)
    coffeHouse.coffes = coffes
    db.session.add(coffeHouse)
    db.session.commit()
    # TODO нужно реализовать этот контроллер всё-таки
    return '{"status:":"ok"}', 204


@app.route('/controller/coffe', methods=['DELETE'])
@cross_origin()
def delete_coffe():
    d = json.loads(request.get_data().decode('utf-8'))
    coffe = Coffe.query.get(int(d['id']))
    path = '/var/www/html/'+str(coffe.photo[-1].filename).split('/')[-1]
    if os.path.exists(path):
        os.remove(path)
        print('file', path, 'is removed')
    db.session.delete(coffe)
    db.session.commit()
    return 'Hello World!'
