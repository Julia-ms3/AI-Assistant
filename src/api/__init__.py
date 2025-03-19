from fastapi import APIRouter

from src.api.routers import router as ai_router
from src.api.websocket import router as wb_router

root_router = APIRouter()
root_router.include_router(ai_router)
root_router.include_router(wb_router)
