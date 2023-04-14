import logging


class XLog(logging.Logger):

    # 初始化 Logger
    def __init__(self,
                 name='root',
                 logger_level='INFO',
                 file=None,
                 logger_format="[%(filename)s:%(lineno)d] %(asctime)s - %(levelname)s - %(message)s"):
        # 1、设置logger收集器，继承logging.Logger
        super().__init__(name)

        # 2、设置日志收集器level级别
        self.setLevel(logger_level)

        # 5、设置 handler 格式
        fmt = logging.Formatter(logger_format, datefmt='%Y-%m-%d %H:%M:%S')

        # 3、设置日志处理器

        # 如果传递了文件，就会输出到file文件中
        if file:
            file_handler = logging.FileHandler(file)
            # 4、设置 file_handler 级别
            file_handler.setLevel(logger_level)
            # 6、设置handler格式
            file_handler.setFormatter(fmt)
            # 7、添加handler
            self.addHandler(file_handler)

        # 默认都输出到控制台
        stream_handler = logging.StreamHandler()
        # 4、设置 stream_handler 级别
        stream_handler.setLevel(logger_level)
        # 6、设置handler格式
        stream_handler.setFormatter(fmt)
        # 7、添加handler
        self.addHandler(stream_handler)


if __name__ == '__main__':
    logger = XLog()
    logger.info("Good")