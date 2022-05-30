import os
from app import app
from app import model, db
import json
from flask import request
from flask import jsonify


@app.route('/coffehouse/get_coffe', methods=['GET', 'POST'])
def getCoffe():
    ''' 
    если url в базе данных не соответсвует переданному, то
    изображение на сервере удаляется, если вместо url передаётся base64 строка,
    то создаётся новое изображение. Метод возвращает новый массив c url картинок
    '''
    #d = json.loads(request.get_data().decode('utf-8'))
    coffeHouse = model.Coffehouse.query.get(int(1))
    coffes = coffeHouse.coffes.all()

    data = list(map(lambda coffe: coffe.toDict(), coffes))
    print(data)
    data = (jsonify(data))

    # TODO нужно реализовать этот контроллер всё-таки
    return data


@app.route('/coffehouse/create_coffe', methods=['GET', 'POST'])
def coffeCreate():
    '''
    получает на вход массив с url изображений
    если url в базе данных не соответсвует переданному, то
    изображение на сервере удаляется, если вместо url передаётся base64 строка,
    то создаётся новое изображение. Метод возвращает новый массив c url картинок
    '''
    d = json.loads(request.get_data().decode('utf-8'))
    coffeHouse = model.Coffehouse.query.get(1)
    coffes = (coffeHouse.coffes)
    coffe = model.Coffe()
    coffe.name = d['name']
    photo = model.Photo()
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
    return '{"starus:":"ok"}'


@app.route('/coffehouse/delete_coffe', methods=['GET', 'POST'])
def coffeDelete():
    d = json.loads(request.get_data().decode('utf-8'))
    coffe = model.Coffe.query.get(int(d['id']))

    path = '/var/www/html/'+str(coffe.photo[-1].filename).split('/')[-1]
    print(path)
    if os.path.exists(path):
        os.remove(path)
        print('file', path, 'is removed')
    db.session.delete(coffe)
    db.session.commit()
    print('deleted coffe ', d['id'])
    return 'Hello World!'
