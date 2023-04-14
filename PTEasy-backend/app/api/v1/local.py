import os
from flask import jsonify, request
from app.libs.x_disk import get_size, get_file_type
from app.libs.redprint import Redprint

redprint = Redprint('local')


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
            # 根据后缀判断文件类型
            file_type = get_file_type(sub_filepath)
            file_size = sub_filepath_info.st_size
        else:
            file_type = "dir"
            file_size = get_size(sub_filepath)

        if file_size != 0:
            tmp = {
                'name': path,
                'path': sub_filepath,
                'size': file_size,
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
