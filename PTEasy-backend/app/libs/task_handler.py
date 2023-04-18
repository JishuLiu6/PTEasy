# task.py
import time

from app.models.LogInfo import LogInfo
from app.models.TaskInfo import TaskInfo
from app.extensions import socketio


class TaskHandler:
    def __init__(self, task_id, task_type, task_len):
        self.task_id = task_id
        self.task_type = task_type
        self.task_len = task_len

    def start_task(self):
        socketio.emit('task:start', {'task_id': self.task_id,
                                     'task_type': self.task_type,
                                     'status': 'running',
                                     'task_data': {'task_len': self.task_len}})
        # 创建任务
        TaskInfo.create(
            {'task_id': self.task_id, 'name': self.task_type, 'type': self.task_type, 'progress': 0, 'status': 1,
             'start_time': int(time.time() * 1000), 'task_len': self.task_len, 'update_time': int(time.time() * 1000),
             'create_user': 1, 'end_time': 0})

        # 添加日志
        LogInfo.create({'task_id': self.task_id, 'level': 0, 'message': f'{self.task_type} 任务开始',
                        'time': int(time.time() * 1000), 'create_user': 1})

    def step_start(self, step_data):
        socketio.emit('task:step_start', {'task_id': self.task_id,
                                          'task_type': self.task_type,
                                          'status': 'running',
                                          'task_data': step_data})

        # 在每一步完成时记录日志
        LogInfo.create({'task_id': self.task_id, 'level': 0,
                        'message': f'{step_data} 任务步骤开始',
                        'time': int(time.time() * 1000), 'create_user': 1})

    def step_completed(self, step_data):
        socketio.emit('task:step_completed', {'task_id': self.task_id,
                                              'task_type': self.task_type,
                                              'status': 'completed',
                                              'task_data': step_data})
        # 读取进度
        task_filter_func = TaskInfo.create_filter_func(TaskInfo.task_id == self.task_id)
        progress = TaskInfo.query(task_filter_func).first().progress

        # 更新任务进度
        TaskInfo.update(task_filter_func, {'progress': progress + 1, 'update_time': int(time.time() * 1000),
                                      'status': 1 if progress + 1 < self.task_len else 2})
        # 在每一步完成时记录日志
        LogInfo.create({'task_id': self.task_id, 'level': 2,
                        'message': f'{step_data} 任务步骤完成',
                        'time': int(time.time() * 1000), 'create_user': 1})
        # 如果任务完成，记录日志
        if progress + 1 == self.task_len:
            LogInfo.create({'task_id': self.task_id, 'level': 2, 'message': f'{self.task_id} 任务完成',
                            'time': int(time.time() * 1000), 'create_user': 1})

            # 任务完成，更新任务结束时间
            TaskInfo.update(task_filter_func,
                            {'end_time': int(time.time() * 1000), 'update_time': int(time.time() * 1000), 'status': 2,
                             'progress': self.task_len})

    def step_error(self, error_message):
        socketio.emit('task:step_error', {'task_id': self.task_id,
                                          'task_type': self.task_type,
                                          'status': 'error',
                                          'task_data': {'message': error_message}})
        # 日志记录
        LogInfo.create(
            {'task_id': self.task_id, 'level': 3, 'message': f'{error_message}',
             'time': int(time.time() * 1000), 'create_user': 1})

