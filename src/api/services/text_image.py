import io
import os

import PIL.Image
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))


async def text_response(content):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[content])

    return response.text


async def image_response(request, img_data: bytes):
    img = PIL.Image.open(io.BytesIO(img_data))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[request, img],
    )
    return response.text
