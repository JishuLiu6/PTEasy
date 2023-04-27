from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Text
from sqlalchemy.orm import relationship

from app.models.Base import DbBase


class LogInfo(DbBase):
    '''
    日志信息表
    '''
    __tablename__ = 'LogInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 日志id
    task_id = Column(String(255), nullable=False)  # 任务id
    task_type = Column(String(255), nullable=False)  # 任务类型 file:文件
    level = Column(Integer, nullable=False)  # 日志级别 0:info 1:warning 2:success 3:error
    message = Column(Text, nullable=False)  # 日志信息
    time = Column(BigInteger, nullable=False)  # 日志时间
    create_user = Column(Integer, nullable=False)  # 用户id

