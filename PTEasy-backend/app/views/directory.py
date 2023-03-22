import os
from flask import jsonify
from app.libs.redprint import Redprint

redprint = Redprint('directory')


@redprint.route('/list', methods=['GET'])
def directory_list():
    os.chdir('./')
    return jsonify({'errno': 1, 'data': os.listdir()})
