from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.Base import DbBase


class TaskInfo(DbBase):
    '''
    任务信息表
    '''
    __tablename__ = 'TaskInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    task_id = Column(Integer, nullable=False)  # 任务id
    name = Column(String(255), nullable=False)  # 任务名称
    type = Column(Integer, nullable=False)  # 任务类型
    task_len = Column(Integer, nullable=False)  # 任务长度
    progress = Column(Integer, nullable=False)  # 任务进度
    status = Column(Integer, nullable=False)  # 任务状态 0:未开始 1:进行中 2:已完成 3:已取消
    start_time = Column(Integer, nullable=False)  # 任务开始时间
    end_time = Column(Integer, nullable=False)  # 任务结束时间
    update_time = Column(Integer, nullable=False)  # 任务更新时间
    create_user = Column(Integer, nullable=False)  # 任务创建人

    # logs = relationship("LogInfo", back_populates="TaskInfo")
