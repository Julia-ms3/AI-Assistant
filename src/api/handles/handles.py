import base64

from src.api.services.text_image import image_response, text_response
from src.api.services.voice import setup_voice

save_img = {'img': []}


async def handle_voice_command():
    return await setup_voice()


async def handle_image(image: str):
    if image:
        save_img['img'].append(image)
        return base64.b64decode(save_img['img'][-1])
    return None


async def handle_text_response(text: str, image_data: bytes = None):
    if image_data:
        return await image_response(text, image_data)
    return await text_response(text)
