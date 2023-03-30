from flask import Flask
from flask_cors import *
from app.api import pc_bp
from app.api.v1 import create_blueprint_v1
from flask_socketio import SocketIO


def register_blueprints(app):
    app.register_blueprint(pc_bp)
    app.register_blueprint(create_blueprint_v1())


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*',async_mode='gevent')
app.config.from_object('app.config.secure')
app.config.from_object('app.config.setting')
register_blueprints(app)
CORS(app, supports_credentials=True)
