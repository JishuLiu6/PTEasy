import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
DATABASE_PATH = os.path.join(BASE_DIR, 'data.db')  # 数据库路径
DATABASE_URL = f"sqlite:///{DATABASE_PATH}" # 数据库连接地址
TOKEN_EXPIRATION = 1 * 24 * 60 * 60  # 1 day
ECHO = False  # 是否打印sql语句
CHECK_SAME_THREAD = False  # 是否检查线程
POOL_SIZE = 100  # 连接池大小
MAX_OVERFLOW = 20  # 超过连接池大小外最多创建的连接
