from sqlalchemy import Column, Integer, String
from app.models.Base import DbBase


class LogInfo(DbBase):
    '''
    日志信息表
    '''
    __tablename__ = 'LogInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 日志id
    level = Column(Integer, nullable=False)  # 日志级别
    message = Column(String(255), nullable=False)  # 日志信息
    time = Column(Integer, nullable=False)  # 日志时间
    user_id = Column(Integer, nullable=False)  # 用户id

