import asyncio
import json
import uuid
from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.libs.disk_scanner_utils import file_task
from app.models.TaskInfo import TaskInfo

task_router = APIRouter()

global_tasks: List[asyncio.Task] = []


@task_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            if message["event"] == "path":
                path = message["payload"]
                taskid = str(uuid.uuid4())
                # background_tasks.add_task(file_task, path, taskid, websocket, 10)
                task = asyncio.create_task(file_task(path, taskid, websocket, 10))
                global_tasks.append(task)  # 添加任务到全局任务列表
    except WebSocketDisconnect:
        # 在 WebSocket 连接关闭时，不再等待所有后台任务完成，让它们继续运行
        pass


@task_router.get("/list")
async def log_list(page: int = 1, size: int = 10):
    total_count = TaskInfo.query().count()

    tasks = TaskInfo.query().order_by(TaskInfo.start_time.desc()).offset(page).limit(size).all()

    # 序列化日志列表
    tasks_serialized = [task.serialize() for task in tasks]

    return {'errno': 0, 'data': {'data_list': tasks_serialized, 'total_count': total_count}}
