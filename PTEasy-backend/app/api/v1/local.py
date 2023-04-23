import os
import uuid
from concurrent.futures import ThreadPoolExecutor

from flask import jsonify, request
from app.libs.x_disk import file_task
from app.libs.redprint import Redprint
tasks = {}
redprint = Redprint('local')
executor = ThreadPoolExecutor(max_workers=4)

@redprint.route('/list', methods=['POST'])
def directory_list():
    rq_data = request.json

    taskid = str(uuid.uuid4())
    executor.submit(file_task, rq_data['path'], taskid, thread_pool_size=3)
    # tasks[taskid] = future

    return jsonify({'errno': 1, 'data': "任务已经开始执行", 'task_id': taskid})


@redprint.route('/status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id')
    if task_id not in tasks:
        return jsonify({'error': '未找到任务', 'task_id': task_id}), 404

    future = tasks[task_id]
    if future.done():
        try:
            result = future.result()
            return jsonify({'status': '完成', 'task_id': task_id, 'result': result})
        except Exception as e:
            return jsonify({'status': '发生错误', 'task_id': task_id, 'error': str(e)})
    else:
        return jsonify({'status': '进行中', 'task_id': task_id})
