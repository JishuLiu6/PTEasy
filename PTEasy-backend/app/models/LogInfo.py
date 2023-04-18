from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.Base import DbBase


class LogInfo(DbBase):
    '''
    日志信息表
    '''
    __tablename__ = 'LogInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 日志id
    task_id = Column(Integer, nullable=False)  # 任务id
    # task_id = Column(Integer, ForeignKey('TaskInfo.id'))  # 任务id
    level = Column(Integer, nullable=False)  # 日志级别 0:info 1:warning 2:success 3:error
    message = Column(String(255), nullable=False)  # 日志信息
    time = Column(Integer, nullable=False)  # 日志时间
    create_user = Column(Integer, nullable=False)  # 用户id

    # task = relationship("TaskInfo", back_populates="LogInfo")

