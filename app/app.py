from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from flask import Flask as _Flask
from datetime import date
from bson import ObjectId


class CustomJSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, ObjectId):
            return str(o)
        raise ServerError()


class Flask(_Flask):
    json_encoder = CustomJSONEncoder
