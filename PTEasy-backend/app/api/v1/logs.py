from flask import jsonify, request

from app.libs.decorators import paginate
from app.libs.redprint import Redprint
from app.models.LogInfo import LogInfo

redprint = Redprint('logs')


@redprint.route('/list', methods=['GET'])
@paginate
def logs_list(offset, size):
    """
    获取日志列表
    :return:
    :params page 页码
    :params size 每页数量
    """
    # 总数
    total_count = LogInfo.query().count()

    logs = LogInfo.query().order_by(LogInfo.time.desc()).offset(offset).limit(size).all()

    # 序列化日志列表
    logs_serialized = [log.serialize() for log in logs]

    return jsonify({'errno': 0, 'data': {'data_list': logs_serialized, 'total_count': total_count}})
