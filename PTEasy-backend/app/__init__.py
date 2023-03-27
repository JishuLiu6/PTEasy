from flask import Flask
from flask_failsafe import failsafe
from flask_cors import *

from app.api import pc_bp
from app.api.v1 import create_blueprint_v1


def register_blueprints(app):
    app.register_blueprint(pc_bp)
    app.register_blueprint(create_blueprint_v1())


@failsafe
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    CORS(app, supports_credentials=True)
    return app


if __name__ == '__main__':
    pass
# https://pypi.douban.com/simple
