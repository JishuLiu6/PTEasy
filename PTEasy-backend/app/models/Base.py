from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config.setting import DATABASE_URL, ECHO, CHECK_SAME_THREAD, POOL_SIZE, MAX_OVERFLOW

# 创建数据库引擎
engine = create_engine(
    url=DATABASE_URL,
    echo=ECHO,
    connect_args={
        'check_same_thread': CHECK_SAME_THREAD
    },
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW
)

# 初始化数据库会话
DBSession = sessionmaker(bind=engine)
Base = declarative_base()


# 定义上下文管理器，用于数据库会话的自动提交和回滚
@contextmanager
def db_session_scope():
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 基础混入类，包含数据库操作的通用方法
class BaseMixin:
    @classmethod
    def query(cls, filter_func=None):
        session = DBSession()
        query = session.query(cls)
        if filter_func:
            query = filter_func(query)
        return query

    def serialize(self, include=None, exclude=None):
        if include is None:
            include = []
        if exclude is None:
            exclude = []

        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}

        # 过滤 include 和 exclude 列表中的列
        filtered_columns = {key: value for key, value in columns.items() if
                            (not include or key in include) and key not in exclude}

        return filtered_columns
    @classmethod
    def create_filter_func(cls, *args, **kwargs):
        def filter_func(query):
            return query.filter(*args).filter_by(**kwargs)

        return filter_func

    # 获取单个记录
    @classmethod
    def get(cls, primary_key):
        cls._ensure_table_exists()
        with db_session_scope() as session:
            result = session.query(cls).get(primary_key)
            return result.serialize() if result else None

    # 创建记录
    @classmethod
    def create(cls, model_dict):
        cls._ensure_table_exists()
        model_instance = cls(**model_dict)
        with db_session_scope() as session:
            session.add(model_instance)

    # 更新记录
    @classmethod
    def update(cls, filter_func, update_dict):
        cls._ensure_table_exists()
        with db_session_scope() as session:
            query = filter_func(session.query(cls))
            query.update(update_dict)

    # 批量更新记录
    @classmethod
    def bulk_update(cls, filter_func, update_dicts):
        cls._ensure_table_exists()
        with db_session_scope() as session:
            query = filter_func(session.query(cls))
            for update_dict in update_dicts:
                query.update(update_dict)

    # 删除记录
    @classmethod
    def delete(cls, primary_key):
        cls._ensure_table_exists()
        with db_session_scope() as session:
            record = session.query(cls).get(primary_key)
            if record:
                session.delete(record)

    # 确保数据库表存在，如果不存在则创建
    @classmethod
    def _ensure_table_exists(cls, force=False):
        if force:
            cls.create_table(cls)
            return
        try:
            with db_session_scope() as session:
                session.query(cls).first()
        except OperationalError:
            cls.create_table(cls)

    # 创建数据库表
    @staticmethod
    def create_table(base=Base):
        base.metadata.create_all(engine)


# DbBase是所有数据库模型的基类，它包含BaseMixin提供的方法
class DbBase(Base, BaseMixin):
    __abstract__ = True
