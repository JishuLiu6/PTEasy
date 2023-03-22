import json
import bson
from bson import ObjectId
from mongoengine import connect, Document

connect(alias='pt-db', db='pt_easy', host='mongodb://root:qwertyuiop@127.0.0.1', authentication_source="admin")


class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class MongoBase(Document):
    # 序列化处理，排除某些字段
    def serialize(self, *args):
        model_dict = self.to_mongo().to_dict()
        model_dict['id'] = model_dict['_id']

        if args:
            list(map(model_dict.pop, list(args)))

        for key in model_dict.keys():
            if isinstance(model_dict[key], bson.objectid.ObjectId):
                model_dict[key] = str(model_dict[key])
        del model_dict['_id']

        return model_dict

    # 序列化处理，只返回特定字段
    def serialize_only(self, *args):
        # print(args)
        model_dict = self.to_mongo().to_dict()
        model_dict['id'] = model_dict['_id']
        if args:
            fields = [i for i in model_dict.keys() if i not in list(args)]
            list(map(model_dict.pop, fields))

        for key in list(args):
            if key not in model_dict:
                model_dict[key] = "——"
                continue
            if isinstance(model_dict[key], bson.objectid.ObjectId):
                model_dict[key] = str(model_dict[key])

        return model_dict

    meta = {
        'abstract': True
    }
