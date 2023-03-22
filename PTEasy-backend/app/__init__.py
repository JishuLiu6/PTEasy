from flask_failsafe import failsafe
from flask_cors import *
from .app import Flask


def register_blueprints(app):
    from app.views import create_blueprint_pt_easy
    app.register_blueprint(create_blueprint_pt_easy())


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
