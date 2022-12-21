
from enum import unique
import hashlib
from app import db
from app import app
from flask import jsonify, request
from flask_cors import cross_origin
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token, jwt_required, get_jwt_identity)


class Auth(db.Model):
    '''
    Модуль содержит таблицу с логином, хэшем пароля, id в таблице авторизации
    и id в таблице с пользователями
    '''
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(120))
    real_id = db.Column(db.Integer)
    password_reset = db.Column(db.Integer)
    password_hash = db.Column(db.String(120))


def generate_password_hash(password):
    '''
    Метод генерирует хэш пароля 
    '''
    salt = b'\x1c\xc5\xc1\xee\t\r\'\xff\xf2\xf4\x12\x1c\xa2\xc9\x98\xa1\xb7\xff}\x05k"A]3\xe18\'\xd6\xb2[P'
    key = hashlib.pbkdf2_hmac('sha256', password.encode(
        'utf-8'), salt, 100000, dklen=128)
    return key


def check_password_hash(password, hash):
    '''
    Проверка соотвествия хэша пароля хэшу в базе данных
    '''

    current_key = generate_password_hash(password)
    if current_key == hash:
        return True
    else:
        return False


def create_user(login: str, password: str, role: str, real_id: int):
    '''
    метод создаёт нового пользователя в системе авторизации
    '''
    if len(login) == 0:
        raise ValueError('login_is_empty')
    if len(password) < 7:
        raise ValueError('weak password')
    if (Auth.query.filter_by(login=login).first() != None):
        raise ValueError('user exist')
    auth = Auth()
    auth.login = login
    auth.password_hash = generate_password_hash(password)
    auth.role = role
    auth.real_id = real_id
    db.session.add(auth)
    db.session.commit()
    return 1


@app.route('/security/auth', methods=['GET'])
@cross_origin()
def auth():
    
    auth = Auth.query.filter_by(
        login=request.authorization.username).first()
    if auth == None:
        return {'status': 'user is not exist'}, 404
    if auth != None:

        if check_password_hash(request.authorization.password, auth.password_hash):
            access_token = create_access_token(identity=auth.id, fresh=True)
            refresh_token = create_refresh_token(auth.id)
            return (jsonify({
                'id': auth.real_id,
                'lifetime': app.config['TOKENS_LIFETIME'],
                'access_token': access_token,
                'refresh_token': refresh_token
            }), 200)


@app.route('/security/refresh', methods=['GET', 'POST'])
@jwt_required(refresh=True)
@cross_origin()
def refreshAccessToken():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    return {'access_token': new_token}, 200
