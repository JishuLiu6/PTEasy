# coding:utf-8
from flask import Blueprint, render_template
from app.api import local


def create_blueprint_pt_easy():
    bp = Blueprint('v1', __name__, static_folder='../templates')

    @bp.route("/")
    def confirm():
        return render_template("index.html")

    local.redprint.register(bp)
    return bp
