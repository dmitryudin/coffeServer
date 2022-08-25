from app import socketio
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token, jwt_required, get_jwt_identity)
from flask import request
from flask_socketio import send, emit

'''
@socketio.on('connect')
@jwt_required()
def handle_connect():
    identity = get_jwt_identity()
    print('Client connected with auth_id ', identity)
    print('current user is', request.sid)
    emit('message', 'dsfasdfasf', room=request.sid)
    print('sending')


@socketio.on('disconnect')
@jwt_required()
def test_disconnect():
    print('Client disconnected', request.sid)


@socketio.on('message')
@jwt_required()
def handle_message(data):
    print('received message: ' + data, 'from', get_jwt_identity())


@socketio.on('leave')
def on_leave(data):
    pass
'''