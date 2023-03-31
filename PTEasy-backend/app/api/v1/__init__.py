from flask import Blueprint
from app.api.v1 import local
from .file_socket import *


def create_blueprint_v1():
    bp = Blueprint('v1', __name__, url_prefix='/v1')
    local.redprint.register(bp)
    return bp
