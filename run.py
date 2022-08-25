import threading
from app import app
from flask_jwt_extended import JWTManager
from app import socketio
from datetime import timedelta

app.config['CORS_HEADERS'] = 'Content-Type'
# socketio = SocketIO(app)
app.config['JWT_SECRET_KEY'] = 'this-is-super-secret'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config['TOKENS_LIFETIME'] = 3000  # 5*60
jwt = JWTManager(app)


#app.run(debug=True, host='2.59.41.249', port=5050)
socketio.run(app, debug=True, host='185.119.58.234', port=5050, )
