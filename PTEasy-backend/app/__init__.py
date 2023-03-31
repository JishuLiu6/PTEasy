from flask import Flask
from flask_cors import CORS
from app.api import pc_bp
from app.api.v1 import create_blueprint_v1
from app.extensions import socketio


def register_blueprints(app):
    app.register_blueprint(pc_bp)
    app.register_blueprint(create_blueprint_v1())


app = Flask(__name__)
socketio.init_app(app)
app.config.from_object('app.config.secure')
app.config.from_object('app.config.setting')
register_blueprints(app)
CORS(app, supports_credentials=True)