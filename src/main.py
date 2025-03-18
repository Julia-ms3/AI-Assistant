from fastapi import FastAPI

from src.api import root_router

app = FastAPI()
app.include_router(root_router)
