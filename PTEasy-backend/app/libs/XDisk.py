import os
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.schedulers.background import BackgroundScheduler
from app.extensions import socketio


# jobstores = {
#     'default': SQLAlchemyJobStore(url=f"sqlite://{os.path.join('/data/', 'socketJobs.db')}")
# }
#
#
# scheduler = BackgroundScheduler(jobstores=jobstores)


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


def get_file_info(file_entry, taskid) -> None:
    '''
    获取目录或文件的大小
    :param file_entry:
    :param taskid:
    :return: t_size
    '''

    try:
        sub_filepath_info = file_entry['stat']
        if file_entry['is_file']:
            file_type = "file"
            file_size = sub_filepath_info.st_size
        else:
            file_type = "dir"
            file_size = get_size(file_entry['path'])

        if file_size != 0:
            atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_atime))
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_mtime))
            from app.models.FileInfo import FileInfoData
            FileInfoData.create({'soft_path': os.path.basename(file_entry['path']),
                                 'file_name': file_entry['path'],
                                 'file_size': file_size,
                                 'file_type': file_type,
                                 'visit_time': atime,
                                 'modify_time': mtime,
                                 'file_id': sub_filepath_info.st_ino,
                                 'parent_id': os.stat(os.path.dirname(file_entry['path'])).st_ino})
            # 发送步骤完成

            socketio.emit('step_file_task', {'task_id': taskid,
                                             'status': 'completed',
                                             'task_data': {'file_path': file_entry['path']}
                                             })
    except Exception as e:
        # 发送步骤错误
        print(traceback.format_exc())
        socketio.emit('step_error', {'task_id': taskid,
                                     'status': 'error',
                                     'task_data': {'message': traceback.format_exc()}})

        return None


def file_task(real_path, taskid) -> None:
    with os.scandir(real_path) as entries:
        entries_list = list(entries)
        total_entries = len(entries_list)
        # socket发送任务长度消息
        socketio.emit('start_file_task', {'task_id': taskid,
                                          'status': 'running',
                                          'task_data': {'task_len': total_entries}})
        for entry in entries_list:
            # 为了序列化记录，这里需要将entry转换为dict
            entry_dict = {
                'stat': entry.stat(),
                'is_file': entry.is_file(),
                'path': entry.path
            }
            with ThreadPoolExecutor() as executor:
                executor.map(lambda x: get_file_info(entry_dict, taskid), [None])
                # executor.map(get_file_info, entry_dict, taskid)
        #     scheduler.add_job(get_file_info, args=(entry_dict, taskid), id=f'{entry.path}_{taskid}')
        # scheduler.start(paused=False)
