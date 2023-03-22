from flask import jsonify
from app.libs.redprint import Redprint

redprint = Redprint('user')

@redprint.route('/hello', methods=['GET'])
def user_hello():
    return jsonify({'errno': 1, 'data': 'hello world'})
