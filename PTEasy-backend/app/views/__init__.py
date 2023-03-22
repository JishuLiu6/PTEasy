# coding:utf-8
from flask import Blueprint
from app.views import user, directory


def create_blueprint_pt_easy():
    bp = Blueprint('pt_easy', __name__)
    user.redprint.register(bp)
    directory.redprint.register(bp)
    return bp
