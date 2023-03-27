from flask import Blueprint, render_template

# 设置静态文件夹为templates，以便于前端打包页面能直接使用
pc_bp = Blueprint('pc', __name__, static_folder='../templates')


@pc_bp.route("/")
@pc_bp.route("/home")
@pc_bp.route("/about")
def root_index():
    return render_template("index.html")
