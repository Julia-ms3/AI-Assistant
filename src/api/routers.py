from fastapi import APIRouter, File, UploadFile

from src.api.services import image_response, text_response

router = APIRouter(tags=['AI Assistant'])


@router.post('/generate_ai_response')
def generate_ai_response(request: str):
    return text_response(request)


@router.post('/upload_image')
def upload_image(request, img_file: UploadFile = File(...)):
    return image_response(request, img_file)
