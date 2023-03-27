from sqlalchemy import Column, Integer, String
from app.models.Base import create_table, Base


# 定义映射类User，其继承上一步创建的Base
class User(Base):
    # 指定本类映射到users表
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    name = Column(String(20))
    fullname = Column(String(32))
    password = Column(String(32))

    # __repr__方法用于输出该类的对象被print()时输出的字符串，如果不想写可以不写
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)



if __name__ == '__main__':
    # create_table(User)
    from app.models.Base import DBSession
    # 创建session对象:
    db = DBSession()
    # 创建新User对象:
    new_user = User(name='1234', fullname='Bob', password="123")
    # 添加到session:
    db.add(new_user)
    # 提交即保存到数据库:
    db.commit()
    # 关闭session:
    db.close()

