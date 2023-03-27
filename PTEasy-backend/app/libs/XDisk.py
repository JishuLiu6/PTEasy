import os


def get_size(path) -> int:
    '''
    递归获取目录或文件的大小
    :param path:
    :return:
    '''
    try:
        t_size = 0
        os.chdir(path)
        child_file_list = os.listdir()  # 获取path目录下所有文件
        for filename in child_file_list:
            child_path = os.path.join(path,filename)  # 获取path与filename组合后的路径
            if os.path.isdir(child_path):   # 判断是否为目录
                t_size += get_size(child_path)        # 是目录就继续递归查找
            elif os.path.isfile(child_path):  # 判断是否为文件
                filesize = os.path.getsize(child_path)  # 如果是文件，则获取相应文件的大小
                t_size += filesize
    except Exception as e:
        t_size = 0
        print("error", path, e)
    return t_size
