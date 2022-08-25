import os
from app import app
from app import db
from app.Models import model
import json
from flask import request
from flask import jsonify
from app.Models.Coffe_house_model import Coffehouse
from app.Models.Dish_model import Dish
from app.Models.Other import Photo
from flask_cors import cross_origin


@app.route('/controllers/coffes', methods=['GET'])
@cross_origin()
def get_dishes():
    ''' 
    если url в базе данных не соответсвует переданному, то
    изображение на сервере удаляется, если вместо url передаётся base64 строка,
    то создаётся новое изображение. Метод возвращает новый массив c url картинок
    '''
    #d = json.loads(request.get_data().decode('utf-8'))
    coffeHouse = Coffehouse.query.get(int(1))
    dishes = coffeHouse.dishes.all()

    data = list(map(lambda dish: dish.toDict(), dishes))
    
    data = (jsonify(data))
    # TODO нужно реализовать этот контроллер всё-таки
    return data


@app.route('/controllers/coffe', methods=['POST'])
@cross_origin()
def dish_create():
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
    dishes = (coffeHouse.dishes)
    dish= Dish()
    dish.name = d['name']
    photo = Photo()
    if d['picture']:
        photo.filename = d['picture'].split('/')[-1]
    dish.picture = [photo]
    dish.category = d['category']
    dish.subcategory = d['subcategory']
    dish.description = d['description']
    dish.weight = d['weight']
    dish.base_price = d['base_price']
    dish.field_selection = str(d['field_selection'])
    dish.options = str(d['options'])
    dishes.append(dish)
    coffeHouse.dishes = dishes
    db.session.add(coffeHouse)
    db.session.commit()
    return '{"status:":"ok"}', 204


@app.route('/controllers/coffe', methods=['DELETE'])
@cross_origin()
def delete_coffe():
    d = json.loads(request.get_data().decode('utf-8'))
    print(d)
    dish = Dish.query.get(d['id'])
    path = '/var/www/html/'+str(dish.picture.first().filename).split('/')[-1]
    if os.path.exists(path):
        os.remove(path)
        print('file', path, 'is removed')
    db.session.delete(dish)
    db.session.commit()
    return {'status':'ok'}
