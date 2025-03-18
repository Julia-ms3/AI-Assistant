from fastapi import APIRouter

from src.api.routers import router as ai_router

root_router = APIRouter()
root_router.include_router(ai_router)
