
from app import socketio
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token, jwt_required, get_jwt_identity)
from flask import request
from flask_socketio import send, emit
from app import app
import json
from app.Models.Order_model import Order
from app.Models.Client_model import Client
from app import db 
from app.Security.JWT import Auth
from flask import jsonify

clients = []

@socketio.on('connect')
#@jwt_required()
def handle_connect():
    clients.append(request.sid)
    print('current user is', request.sid)
    
    #emit('message', 'dsfasdfasf', room=request.sid)



@socketio.on('disconnect')
#@jwt_required()
def test_disconnect():
    clients.remove(request.sid)
    print('Client disconnected', request.sid)




@app.route('/controllers/accept_order', methods=['GET'])
def accept_order():
    order_id = request.args.get('order_id')
    order = Order.query.get(order_id)
    order.is_accepted = True
    db.session.commit()
    return {"status":"ok"}

@app.route('/controllers/order_completed', methods=['GET'])
def order_completed():
    order_id = request.args.get('order_id')
    order = Order.query.get(order_id)
    order.is_active = False
    db.session.commit()
    return {"status":"ok"}

@app.route('/controllers/order_ready', methods=['GET'])
def order_ready():
    order_id = request.args.get('order_id')
    order = Order.query.get(order_id)
    order.is_ready = True
    db.session.commit()
    return {"status":"ok"}

@app.route('/controllers/history_orders', methods=['GET'])
def get_history_orders():
    orders = db.session.query(Order).filter_by(is_active=False).all()
    mapped_active_order = list(map(lambda x: (x.toJson()), orders))
    return jsonify(mapped_active_order)


@app.route('/controllers/active_orders', methods=['GET'])
def get_active_orders():
    orders = db.session.query(Order).filter_by(is_active=True).all()
    mapped_active_order = list(map(lambda x: (x.toJson()), orders))
    return jsonify(mapped_active_order)


@app.route('/controllers/history_orders_by_user_id', methods=['GET'])
def get_history_orders_by_user_id():
    user_id = request.args.get('user_id')
    user = Client.query.get(user_id)
    orders = user.orders
    history_orders = []
    for order in orders:
        if not order.is_active:
            history_orders.append(order)  
    mapped_history_order = list(map(lambda x: x.toJson(), history_orders))
    return jsonify(mapped_history_order)
    return {}

@app.route('/controllers/active_orders_by_user_id', methods=['GET'])
def get_orders_active_orders_by_user_id():
    user_id = request.args.get('user_id')
    user = Client.query.get(user_id)
    orders = user.orders  
    active_orders = []
    for order in orders:
        if order.is_active:
            active_orders.append(order)  
    mapped_active_order = list(map(lambda x: x.toJson(), active_orders))
    return jsonify(mapped_active_order)
  

@app.route('/controllers/order', methods=['GET'])
def get_order():
    order_id = request.args.get('order_id')
    order = Order.query.get(order_id)
    return (order.toJson())

@app.route('/controllers/order', methods=['DELETE'])
def delete_order():
    d = json.loads(request.get_data().decode('utf-8'))
    order = Order.query.get(d['order_id'])
    try:
        db.session.delete(order)
        db.session.commit()
    except: pass
    return {"status":"ok"}, 200


@app.route('/controllers/order', methods=['POST'])
@jwt_required()
def create_order():
    d = json.loads(request.get_data().decode('utf-8'))
    userId = Auth.Auth.query.get(get_jwt_identity()).real_id
    order = Order()
    order.user_id = userId
    order.id_payment = d['id_payment']
    order.total_cost = d['total_cost']
    order.on_place = d['on_place']
    order.required_datetime = d['required_date_time']
    order.positions = str(d['order'])
    order.client_id = userId
    order.is_active = True
    order.is_ready = False
    order.is_accepted = False
    order.is_payd_for = False
    db.session.add(order)
    db.session.commit()
    db.session.refresh(order)
    try:
        socketio.emit('message', 'dsfasdfasf', room=clients[-1])
    except: 
        pass
    return {"order_id":order.id}


