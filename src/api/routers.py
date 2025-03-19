import base64
import os

from fastapi import APIRouter, File, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.api.services import image_response, text_response

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


save_img = {'img': []}


@router.websocket("/wb")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            text = data['text']
            image = data.get("image", None)

            await websocket.send_text(f'you: {text}')
            if image:
                save_img['img'].append(image)

            if save_img['img']:

                image_data = base64.b64decode(save_img['img'][-1])
                response = image_response(text, image_data)
                await websocket.send_text(f"assistance: {response}")
            else:
                response = await text_response(text)
                await websocket.send_text(f"assistance:  {response}")


    except WebSocketDisconnect:
        print('Disconnect')
