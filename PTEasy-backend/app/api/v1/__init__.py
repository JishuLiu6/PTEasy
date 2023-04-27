from fastapi import APIRouter
from app.api.v1.file import file_router
from app.api.v1.logs import logs_router
from app.api.v1.task import task_router

v1_router = APIRouter()

v1_router.include_router(file_router, prefix="/file")
v1_router.include_router(task_router, prefix="/task")
v1_router.include_router(logs_router, prefix="/logs")