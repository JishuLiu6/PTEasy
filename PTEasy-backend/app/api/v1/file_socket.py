import uuid

from app.extensions import socketio
from app.libs.x_disk import file_task


@socketio.on('startFileTask')
def start_file_task(path):
    # 处理任务
    taskid = str(uuid.uuid4())
    file_task(path, taskid)
