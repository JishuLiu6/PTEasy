from mongoengine import StringField

from app.models.MongoBase import MongoBase


class DownloadSoftware(MongoBase):
    server_name = StringField()  # 服务器名称
    server_ip = StringField(required=True)  # 服务器IP
    server_port = StringField(required=True)  # 服务器端口
    server_user = StringField(required=True)  # 服务器用户名
    server_pwd = StringField(required=True)  # 服务器密码
    server_type = StringField()  # 服务器类型
    server_desc = StringField()  # 服务器描述
    server_status = StringField()  # 服务器状态

    meta = {'db_alias': 'pt-db'}
