import time
from enum import Enum
from app.models.LogInfo import LogInfo
from app.models.TaskInfo import TaskInfo
from app.extensions import socketio


class LogLevel(Enum):
    INFO = 0
    WARNING = 1
    SUCCESS = 2
    ERROR = 3


class TaskHandler:
    def __init__(self, task_id, task_type, task_name):
        self.task_id = task_id
        self.task_type = task_type
        self.task_len = 0
        self.task_name = task_name

    def _emit_log(self, now_time, level, message):
        # Emit a log message through the socket and save it to the database
        socketio.emit('log', {'task_id': self.task_id,
                              'task_type': self.task_type,
                              'level': level.value, 'message': message,
                              'time': now_time})
        LogInfo.create({'task_id': self.task_id, 'task_type': self.task_type, 'level': level.value, 'message': message,
                        'time': now_time, 'create_user': 1})

    def _update_task(self, task_data):
        # Update the task information in the database and emit a task:update event
        task_filter_func = TaskInfo.create_filter_func(TaskInfo.task_id == self.task_id)
        TaskInfo.update(task_filter_func, task_data)
        socketio.emit('task:update', task_data)

    def _add_task(self, task_data):
        # Add a new task to the database and emit a task:add event
        TaskInfo.create(task_data)
        socketio.emit('task:add', task_data)


    def step(self, level, message, task_len=0, is_child=False):
        if task_len > 0:
            self.task_len = task_len
        now_time = int(time.time() * 1000)

        task_filter_func = TaskInfo.create_filter_func(TaskInfo.task_id == self.task_id)
        task = TaskInfo.query(task_filter_func).first()

        if not task:
            # 无任务，创建任务
            task_data = {'task_id': self.task_id, 'name': self.task_name, 'type': self.task_type, 'progress': 0,
                         'status': 1, 'start_time': now_time, 'task_len': self.task_len,
                         'update_time': now_time, 'create_user': 1, 'end_time': 0}
            self._add_task(task_data)
            progress = 0
        else:
            # 有任务，更新任务
            if not is_child:
                # 父任务
                progress = task.progress
                task_data = {'task_id': self.task_id, 'progress': progress + 1, 'update_time': now_time}
                self._update_task(task_data)

        if progress + 1 >= self.task_len:
            # 任务完成
            task_data.update({'status': 2, 'end_time': now_time})
            self._emit_log(now_time, LogLevel.SUCCESS, f'{self.task_len}个任务完成')
        else:
            # 任务未完成
            self._emit_log(now_time, level, message)

if __name__ == '__main__':
    # Create a TaskHandler instance and perform a sample step
    task_handler = TaskHandler("task1", "task_type1", "Sample Task")
    task_handler.step(LogLevel.INFO, "Starting the task...")
