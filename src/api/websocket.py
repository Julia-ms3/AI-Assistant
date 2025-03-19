
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.api.handles.handles import (handle_image, handle_text_response,
                                     handle_voice_command)

router = APIRouter(tags=['AI Assistant'])


@router.websocket("/wb")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()

            text = data.get("text", '')
            image = data.get("image", None)
            command = data.get("command")

            if command == "voice":
                text = await handle_voice_command()

            image_data = await handle_image(image)

            response = await handle_text_response(text, image_data)

            await websocket.send_text(f'you: {text}')
            await websocket.send_text(f"assistance: {response}")

    except WebSocketDisconnect:
        print('Disconnect')
