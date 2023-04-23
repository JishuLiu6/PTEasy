# task.py
import threading
import time

from app.models.LogInfo import LogInfo
from app.models.TaskInfo import TaskInfo
from app.extensions import socketio


class TaskHandler:
    def __init__(self, task_id, task_type, task_name):
        self.task_id = task_id
        self.task_type = task_type
        self.task_len = 0
        self.task_name = task_name
        # self.progress_lock = threading.Lock()

    def start_task(self, task_len):
        self.task_len = task_len
        socketio.emit('task:add',
                      {'task_id': self.task_id, 'name': self.task_name, 'type': self.task_type, 'progress': 0,
                       'status': 1,
                       'start_time': int(time.time() * 1000), 'task_len': self.task_len,
                       'update_time': int(time.time() * 1000),
                       'create_user': 1, 'end_time': 0})
        # 创建任务
        TaskInfo.create(
            {'task_id': self.task_id, 'name': self.task_name, 'type': self.task_type, 'progress': 0, 'status': 1,
             'start_time': int(time.time() * 1000), 'task_len': self.task_len, 'update_time': int(time.time() * 1000),
             'create_user': 1, 'end_time': 0})
        # 添加日志
        socketio.emit('log', {'task_id': self.task_id,
                              'task_type': self.task_type,
                              'level': 2, 'message': f'任务开始，共{self.task_len}个步骤',
                              'time': int(time.time() * 1000)})
        LogInfo.create({'task_id': self.task_id,
                        'task_type': self.task_type,
                        'level': 2, 'message': f'任务开始，共{self.task_len}个步骤',
                        'time': int(time.time() * 1000), 'create_user': 1})

    def step_start(self, step_data):
        socketio.emit('log', {'task_id': self.task_id, 'level': 0,
                              'task_type': self.task_type,
                              'message': f'{step_data} 步骤开始',
                              'time': int(time.time() * 1000)})
        LogInfo.create({'task_id': self.task_id, 'level': 0,
                        'task_type': self.task_type,
                        'message': f'{step_data} 步骤开始',
                        'time': int(time.time() * 1000), 'create_user': 1})

    def step_completed(self, step_data):
        # 读取进度
        task_filter_func = TaskInfo.create_filter_func(TaskInfo.task_id == self.task_id)

        # 更新任务进度
        # with self.progress_lock:
        progress = TaskInfo.query(task_filter_func).first().progress
        socketio.emit('task:update', {'task_id': self.task_id,
                                      'progress': progress + 1,
                                      'update_time': int(time.time() * 1000),
                                      'status': 1 if progress + 1 < self.task_len else 2})
        TaskInfo.update(task_filter_func, {'progress': progress + 1, 'update_time': int(time.time() * 1000)})
        # 在每一步完成时记录日志
        socketio.emit('log', {'task_id': self.task_id, 'level': 2,
                              'task_type': self.task_type,
                              'message': f'{step_data} 步骤完成',
                              'time': int(time.time() * 1000)})
        LogInfo.create({'task_id': self.task_id, 'level': 2,
                        'task_type': self.task_type,
                        'message': f'{step_data} 步骤完成',
                        'time': int(time.time() * 1000), 'create_user': 1})
        # 如果任务完成，记录日志
        if progress+1 >= self.task_len:
            socketio.emit('log', {'task_id': self.task_id, 'level': 2,
                                  'task_type': self.task_type,
                                  'message': f'{self.task_len} 任务完成',
                                  'time': int(time.time() * 1000)})
            LogInfo.create({'task_id': self.task_id, 'level': 2,
                            'task_type': self.task_type,
                            'message': f'{self.task_len} 任务完成',
                            'time': int(time.time() * 1000), 'create_user': 1})

            socketio.emit('task:update', {'task_id': self.task_id,
                                          'end_time': int(time.time() * 1000),
                                          'update_time': int(time.time() * 1000), 'status': 2,
                                          'progress': self.task_len})

            TaskInfo.update(task_filter_func,
                            {'end_time': int(time.time() * 1000), 'update_time': int(time.time() * 1000), 'status': 2})

    def step_warning(self, warning_message):
        socketio.emit('log', {'task_id': self.task_id,
                              'task_type': self.task_type,
                              'level': 1, 'message': f'{warning_message}',
                              'time': int(time.time() * 1000)})
        # 日志记录
        LogInfo.create(
            {'task_id': self.task_id,
             'task_type': self.task_type,
             'level': 1, 'message': f'{warning_message}',
             'time': int(time.time() * 1000), 'create_user': 1})

    def step_info(self, info_message):
        socketio.emit('log', {'task_id': self.task_id,
                              'task_type': self.task_type,
                              'level': 0, 'message': f'{info_message}',
                              'time': int(time.time() * 1000)})
        # 日志记录
        LogInfo.create(
            {'task_id': self.task_id,
             'task_type': self.task_type,
             'level': 0, 'message': f'{info_message}',
             'time': int(time.time() * 1000), 'create_user': 1})

    def step_error(self, error_message):
        socketio.emit('log', {'task_id': self.task_id,
                              'task_type': self.task_type,
                              'level': 3, 'message': f'{error_message}',
                              'time': int(time.time() * 1000)})
        # 日志记录
        LogInfo.create(
            {'task_id': self.task_id,
             'task_type': self.task_type,
             'level': 3, 'message': f'{error_message}',
             'time': int(time.time() * 1000), 'create_user': 1})
