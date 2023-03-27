from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    url="sqlite:///data.db",
    echo=False,  # 打开sqlalchemy ORM过程中的详细信息
    connect_args={
        'check_same_thread': True  # 是否多线程
    }
)

Base = declarative_base()
DBSession = sessionmaker(bind=engine)


# 创建表
def create_table(base=Base):
    base.metadata.create_all(engine)
