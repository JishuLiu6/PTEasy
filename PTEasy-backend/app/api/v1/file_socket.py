from app import socketio


@socketio.on('startFileTask')
def start_file_task(data):
    print(data)
    # 处理任务
    # file_task(real_path, taskid, socketio)
