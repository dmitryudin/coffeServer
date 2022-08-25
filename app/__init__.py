
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_folder="/root/coffeServer/app/web",
            template_folder='/root/coffeServer/app/web')
app.config.from_object('config')
db = SQLAlchemy(app)

socketio = SocketIO(app)
#from app.Security.JWT import Auth
from app.Controllers import ClientController, DishController, CoffeHouseController, OrderController, RemoteFileManager
from app.Models import Client_model, Coffe_house_model, Dish_model, Order_model, Other
from app.ChatEngine import Chat_model
from app.Security.JWT import Auth
from app.Security import FormValidator
from app.ChatEngine import Chat_controller
from app import app
