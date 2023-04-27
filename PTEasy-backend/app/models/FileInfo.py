from sqlalchemy import Column, Integer, String, BigInteger
from app.models.Base import DbBase


class FileInfo(DbBase):
    '''
    文件信息表
    '''
    __tablename__ = 'FileInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    soft_path = Column(String(255), nullable=False)  # 软路径
    file_name = Column(String(255), nullable=False)  # 文件名
    file_size = Column(Integer, nullable=False)  # 文件大小
    visit_time = Column(BigInteger, nullable=False)  # 访问时间
    last_visit_time = Column(BigInteger)  # 上次访问时间
    modify_time = Column(BigInteger, nullable=False)  # 修改时间
    last_modify_time = Column(BigInteger)  # 上次修改时间
    file_id = Column(BigInteger, nullable=False)  # 文件id
    parent_id = Column(Integer, nullable=False)  # 目录id
    file_type = Column(String(255), nullable=False)  # 文件类型
    is_delete = Column(Integer, nullable=False, default=0)  # 是否已经删除


if __name__ == '__main__':
    pass
    # data = {
    #     'soft_path': '/path/to/file',
    #     'file_name': 'test.txt',
    #     'file_size': 1024,
    #     'create_time': 1234567890,
    #     'modify_time': 1234567890,
    #     'parent_id': 1,
    #     'file_type': 'txt'
    # }
    # file_info = FileInfoData.create(data)

    # FileInfoData.create_table()
    # create_table()
    # create_table(FileInfo)
    # from app.models.Base import DBSession
    # # 创建session对象:
    # db = DBSession()
    # # 创建新User对象:
    # new_user = User(name='1234', fullname='Bob', password="123")
    # # 添加到session:
    # db.add(new_user)
    # # 提交即保存到数据库:
    # db.commit()
    # # 关闭session:
    # db.close()
