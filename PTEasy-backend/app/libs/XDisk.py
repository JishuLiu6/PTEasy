import os
import time
from concurrent.futures import ThreadPoolExecutor



def get_size(path) -> int:
    '''
    获取目录或文件的大小
    :param path:
    :return: t_size
    '''

    if os.path.isfile(path):
        t_size = os.path.getsize(path)
    elif os.path.isdir(path):
        t_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                t_size += os.path.getsize(os.path.join(dirpath, filename))
    else:
        t_size = 0
    return t_size


def get_file_info(file_entry, taskid=None, socket=None) -> None:
    '''
    获取目录或文件的大小
    :param file_entry:
    :param taskid:
    :param socket:
    :return: t_size
    '''
    try:
        sub_filepath_info = file_entry.stat()
        if file_entry.is_file():
            file_type = "file"
            file_size = sub_filepath_info.st_size
        else:
            file_type = "dir"
            file_size = get_size(file_entry.path)

        if file_size != 0:
            ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_ctime))
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_mtime))
            from app.models.FileInfo import FileInfoData
            FileInfoData.create(**{'soft_path': os.path.basename(file_entry.path),
                                   'file_name': file_entry.path,
                                   'file_size': file_size,
                                   'file_type': file_type,
                                   'create_time': ctime,
                                   'modify_time': mtime,
                                   'parent_id': os.stat(os.path.dirname(file_entry.path)).st_ino})
            if socket:
                # 发送步骤完成
                socket.emit('step_progress',
                            {'task_id': taskid, 'data': {'file_path': file_entry.path}, 'status': 'step_done'})
    except Exception as e:
        # 发送步骤错误
        socket.emit('error_progress', {'task_id': taskid, 'data': str(e), 'status': 'step_error'})
        return None


def file_task(real_path, taskid, socket) -> None:
    with os.scandir(real_path) as entries:
        total_entries = len(list(entries))
        # socket发送任务长度消息
        socket.emit('start_progress', {'task_id': taskid, 'data': {'task_len': total_entries}, 'status': 'running'})
        with ThreadPoolExecutor() as executor:
            executor.map(get_file_info, entries, taskid, socket)
        # 等待所有任务完成
        executor.shutdown(wait=True)
        socket.emit('completed_progress', {'task_id': taskid, 'status': 'completed'})
