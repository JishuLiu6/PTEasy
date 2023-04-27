from fastapi import APIRouter

from app.models.LogInfo import LogInfo

logs_router = APIRouter()


@logs_router.get("/list")
async def log_list(page: int = 1, size: int = 10):
    total_count = LogInfo.query().count()

    logs = LogInfo.query().order_by(LogInfo.time.desc()).offset(page).limit(size).all()

    logs_serialized = [log.serialize() for log in logs]

    return {'errno': 0, 'data': {'data_list': logs_serialized, 'total_count': total_count}}
