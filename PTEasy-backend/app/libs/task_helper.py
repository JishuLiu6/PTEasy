import asyncio
import time
from enum import Enum

from app.libs.log_utils import XLog
from app.models.LogInfo import LogInfo
from app.models.TaskInfo import TaskInfo, TaskStatus
from fastapi import WebSocket


class LogLevel(Enum):
    INFO = 0
    WARNING = 1
    SUCCESS = 2
    ERROR = 3


class TaskHandler:
    def __init__(self, task_id, task_type, task_name, websocket: WebSocket = None):
        self.task_id = task_id
        self.task_type = task_type
        self.task_len = 0
        self.task_name = task_name
        self.websocket = websocket
        self.lock = asyncio.Lock()  # 添加一个异步锁

    async def _emit_log(self, now_time, level, message):
        # Emit a log message through the WebSocket and save it to the database
        if self.websocket:
            log_data = {'task_id': self.task_id,
                        'task_type': self.task_type,
                        'level': level.value, 'message': message,
                        'time': now_time}
            # XLog.info(f"Sending message: {log_data}")
            await self.websocket.send_json({'event': 'log', 'payload': log_data})
            await asyncio.sleep(0.1)
            # XLog.info(f"Message sent: {log_data}")

        LogInfo.create({'task_id': self.task_id, 'task_type': self.task_type, 'level': level.value, 'message': message,
                        'time': now_time, 'create_user': 1})

    async def _update_task(self, task_data):
        if self.websocket:
            await self.websocket.send_json({'event': 'task:update', 'payload': task_data})
            await asyncio.sleep(0.1)
        task_filter_func = TaskInfo.create_filter_func(TaskInfo.task_id == self.task_id)
        TaskInfo.update(task_filter_func, task_data)

    async def _add_task(self, task_data):
        # Add a new task to the database and send a task:add event
        if self.websocket:
            await self.websocket.send_json({'event': 'task:add', 'payload': task_data})
            await asyncio.sleep(0.1)
        TaskInfo.create(task_data)
        # socketio.emit('task:add', task_data)

    async def step(self, level, message, task_len=0):
        if task_len > 0:
            self.task_len = task_len
        now_time = int(time.time() * 1000)

        task_filter_func = TaskInfo.create_filter_func(TaskInfo.task_id == self.task_id)
        task = TaskInfo.query(task_filter_func).first()
        progress = task.progress if task else 0

        if not task:
            # 无任务，创建任务
            task_data = {'task_id': self.task_id, 'name': self.task_name, 'type': self.task_type, 'progress': 0,
                         'status': TaskStatus.IN_PROGRESS.value, 'start_time': now_time, 'task_len': self.task_len,
                         'update_time': now_time, 'create_user': 1, 'end_time': 0}
            await self._add_task(task_data)
        elif level.value == LogLevel.SUCCESS.value:
            task_data = {'task_id': self.task_id, 'progress': progress + 1, 'update_time': now_time}
            if progress + 1 == self.task_len:
                # 任务完成
                task_data.update({'status': TaskStatus.COMPLETED.value, 'end_time': now_time})
                async with self.lock:
                    await self._emit_log(now_time, level, f'{self.task_len}个任务完成')
            else:
                # 任务未完成
                async with self.lock:
                    await self._emit_log(now_time, level, message)
            await self._update_task(task_data)
        else:
            async with self.lock:
                await self._emit_log(now_time, level, message)



if __name__ == '__main__':
    # Create a TaskHandler instance and perform a sample step
    task_handler = TaskHandler("task1", "task_type1", "Sample Task")
    task_handler.step(LogLevel.INFO, "Starting the task...")
