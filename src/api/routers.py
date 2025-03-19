import os

from fastapi import APIRouter, File, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.api.services import image_response, text_response

router = APIRouter(tags=['AI Assistant'])


@router.post('/generate_ai_response')
def generate_ai_response(request: str):
    return text_response(request)


@router.post('/upload_image')
def upload_image(request, img_file: UploadFile = File(...)):
    return image_response(request, img_file)


router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/")
async def get_home():
    return FileResponse(os.path.join("static", "index.html"))


@router.websocket("/wb")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"you:  {data}")

            response = await text_response(data)
            await websocket.send_text(f"assistance: {response}")

    except WebSocketDisconnect:
        print('Disconnect')
