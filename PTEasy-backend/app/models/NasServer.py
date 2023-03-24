from mongoengine import StringField
from app.models.MongoBase import MongoBase


class NasServer(MongoBase):
    server_name = StringField()  # 服务器名称
    server_ip = StringField(required=True)  # 服务器IP
    server_port = StringField(required=True)  # 服务器端口
    server_user = StringField(required=True)  # 服务器用户名
    server_pwd = StringField(required=True)  # 服务器密码
    server_type = StringField()  # 服务器类型
    server_desc = StringField()  # 服务器描述
    server_status = StringField()  # 服务器状态

    meta = {'db_alias': 'pt-db'}


if __name__ == '__main__':
    NasServer(**{
        "server_name": '黑群晖1',
        "server_ip": '192.168.195.100',
        "server_port": '5000',
        "server_user": 'jishuliu620',
        "server_pwd": 'Lzw990620',
        "server_type": 'synology',
        "server_desc": '黑群晖, 用于临时存储数据',
        "server_status": '1'
    }).save()