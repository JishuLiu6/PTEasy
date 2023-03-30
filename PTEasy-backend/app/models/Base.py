from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    url="sqlite:///data.db",
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
        with DBSession() as session:
            model_instance = cls(**model_dict)
            session.add(model_instance)
            session.commit()

    @staticmethod
    def read(model_class, filter_args=None):
        with DBSession() as session:
            query = session.query(model_class)
            if filter_args:
                query = query.filter_by(**filter_args)
            result = query.all()
            return [row.__dict__ for row in result]

    @staticmethod
    def update(model_instance):
        with DBSession() as session:
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
#
# def create_table(base=Base):
#     base.metadata.create_all(engine)
# if __name__ == '__main__':
# Base.metadata.create_all(engine)
