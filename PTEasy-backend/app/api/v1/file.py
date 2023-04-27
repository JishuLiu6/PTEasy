from fastapi import APIRouter

file_router = APIRouter()


@file_router.post("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
