from flask import jsonify

from libs.redprint import Redprint

redprint = Redprint('user')


@redprint.route('/hello', methods=['GET'])
def user_hello():
    return jsonify({'errno': 1, 'data': 'not Valid!'})
