import os

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.api.services.text_image import image_response, text_response

router = APIRouter(tags=['AI Assistant'])


@router.post('/generate_ai_response')
async def generate_ai_response(request: str):
    return text_response(request)


@router.post('/upload_image')
async def upload_image(request, img_file: UploadFile = File(...)):
    img_data = img_file.file.read()
    return image_response(request, img_data)


router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/")
async def get_home():
    return FileResponse(os.path.join("static", "index.html"))
