import os

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    url=f"sqlite://{os.path.join('/data/', 'data.db')}",
    echo=False,  # 打开sqlalchemy ORM过程中的详细信息
    connect_args={
        'check_same_thread': True  # 是否多线程
    }
)
DBSession = sessionmaker(bind=engine)
Base = declarative_base()


class DbBase(Base):
    __abstract__ = True

    @classmethod
    def create(cls, model_dict):
        model_instance = cls(**model_dict)
        with DBSession() as session:
            try:
                session.add(model_instance)
                session.commit()
            except OperationalError as e:
                session.rollback()
                cls.create_table(cls)
                session.add(model_instance)
                session.commit()

    @staticmethod
    def delete(model_instance):
        with DBSession() as session:
            session.delete(model_instance)
            session.commit()

    @staticmethod
    def create_table(base=Base):
        base.metadata.create_all(engine)
