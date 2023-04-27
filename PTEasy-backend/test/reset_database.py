from app.models.Base import Base, engine
from app.models.LogInfo import LogInfo
from app.models.TaskInfo import TaskInfo
from app.models.FileInfo import FileInfo


def reset_database():
    # 删除所有数据表
    Base.metadata.drop_all(engine)

    # 创建所有数据表
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    reset_database()
