import os
from flask import jsonify, request
from app.libs.redprint import Redprint

redprint = Redprint('local')


def get_size(path):
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





@redprint.route('/list', methods=['POST'])
def directory_list():
    rq_data = request.json
    current_path = rq_data['path']
    real_path = os.path.realpath(current_path)
    real_path_info = os.stat(real_path)
    parent_id = real_path_info.st_ino
    os.chdir(real_path)
    result = []
    for path in os.listdir():
        sub_filepath = os.path.join(real_path, path)
        sub_filepath_info = os.stat(sub_filepath)
        if os.path.isfile(sub_filepath):
            file_type = "file"
            file_size = sub_filepath_info.st_size
        else:
            file_type = "dir"
            file_size = get_size(sub_filepath)
        # print(sub_filepath, file_size)
        if file_size != 0:
            tmp = {
                'name': path,
                'path': sub_filepath,
                'size': file_size/1024/1024/1024,
                'type': file_type,
                'create_time': sub_filepath_info.st_ctime,
                   'modify_time': sub_filepath_info.st_mtime,
                'parent_id': parent_id
            }
            result.append(tmp)

    return jsonify({'errno': 1, 'data': {
        'current_path': real_path,
        'sub_file_list': result
    }})
