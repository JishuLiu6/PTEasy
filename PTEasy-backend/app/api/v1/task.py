from flask import jsonify, request

from app.libs.decorators import paginate
from app.libs.redprint import Redprint
from app.models.TaskInfo import TaskInfo

redprint = Redprint('task')


@redprint.route('/list', methods=['GET'])
@paginate
def task_list(offset, size):
    """
    获取任务
    :return:
    :params page 页码
    :params size 每页数量
    """
    # 总数
    total_count = TaskInfo.query().count()

    tasks = TaskInfo.query().order_by(TaskInfo.start_time.desc()).offset(offset).limit(size).all()

    # 序列化日志列表
    tasks_serialized = [task.serialize() for task in tasks]

    return jsonify({'errno': 0, 'data': {'data_list': tasks_serialized, 'total_count': total_count}})
