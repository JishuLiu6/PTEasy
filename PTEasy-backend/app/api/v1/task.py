import asyncio
import json
import uuid
from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.libs.disk_scanner_utils import file_task
from app.libs.task_helper import WebSocketHandler, TaskProcessor
from app.models.TaskInfo import TaskInfo

task_router = APIRouter()

global_tasks: List[asyncio.Task] = []


@task_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global global_tasks
    await websocket.accept()
    message_queue = asyncio.Queue()

    # 创建WebSocketHandler实例
    websocket_handler = WebSocketHandler(websocket=websocket, message_queue=message_queue)
    websocket_handler_task = asyncio.create_task(websocket_handler.process_messages())

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            if message["event"] == "path":
                path = message["payload"]
                taskid = str(uuid.uuid4())

                # 创建TaskProcessor实例
                task_processor = TaskProcessor(task_id=taskid, task_type='file_task', task_name='File Task',
                                               websocket=websocket, message_queue=message_queue)
                task = asyncio.create_task(file_task(path, task_processor))

                global_tasks.append(task)

                # 当任务完成时，从全局任务列表中移除
                completed_tasks, _ = await asyncio.wait(global_tasks, return_when=asyncio.FIRST_COMPLETED)
                global_tasks = [t for t in global_tasks if t not in completed_tasks]

    except WebSocketDisconnect:
        websocket_handler_task.cancel()


@task_router.get("/list")
async def log_list(page: int = 1, size: int = 10):
    total_count = TaskInfo.query().count()

    tasks = TaskInfo.query().order_by(TaskInfo.start_time.desc()).offset(page).limit(size).all()

    # 序列化日志列表
    tasks_serialized = [task.serialize() for task in tasks]

    return {'errno': 0, 'data': {'data_list': tasks_serialized, 'total_count': total_count}}
