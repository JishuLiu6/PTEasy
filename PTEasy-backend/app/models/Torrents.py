from mongoengine import StringField, IntField

from app.models.MongoBase import MongoBase


class Torrents(MongoBase):
    server_id = StringField()  # 服务器ID
    torrent_path = StringField()  # 种子存储文件夹
    torrent_cnt = IntField()  # 种子数量
    torrent_size = IntField()  # 种子总大小
    torrent_save_cnt = IntField()  # 保种数量
    meta = {'db_alias': 'pt-db'}
