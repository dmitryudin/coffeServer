


from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_folder="/root/coffeServer/app/web",
            template_folder='/root/coffeServer/app/web')
app.config.from_object('config')
db = SQLAlchemy(app)
from app import app, ClientController, model, security, CoffeController, CoffeHouseController, flutter, RemoteFileManager