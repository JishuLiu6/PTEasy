# coding:utf-8

from flask import Blueprint

from app.views import user


def create_blueprint_pt_easy():
    bp = Blueprint('employ', __name__)
    user.redprint.register(bp)
    return bp
