import os
import uuid
from concurrent.futures import ThreadPoolExecutor

from flask import jsonify, request
from app.libs.x_disk import get_size, get_file_type, file_task
from app.libs.redprint import Redprint

redprint = Redprint('local')
executor = ThreadPoolExecutor(max_workers=4)

@redprint.route('/list', methods=['POST'])
def directory_list():
    rq_data = request.json

    taskid = str(uuid.uuid4())
    # executor.submit(file_task, rq_data['path'], taskid)
    file_task(rq_data['path'], taskid)

    return jsonify({'errno': 1, 'data': "任务已经开始执行"})
