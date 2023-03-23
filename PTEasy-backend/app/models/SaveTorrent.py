from mongoengine import StringField, ListField

from app.models.MongoBase import MongoBase


class SaveTorrent(MongoBase):
    torrents_id = StringField()  # 服务器种子存储路径ID
    name = StringField()  # 种子名称
    size = StringField()  # 种子大小
    tags = ListField()  # 标签
    save_software = StringField()  # 保种软件
    save_file_path = StringField()  # 保种路径
    meta = {'db_alias': 'pt-db'}
