import io
import os

import PIL.Image
from dotenv import load_dotenv
from fastapi import UploadFile
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))


async def text_response(content):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[content])

    return response.text


def image_response(request, img_file: UploadFile):
    img_data = img_file.file.read()
    img = PIL.Image.open(io.BytesIO(img_data))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[request, img],
    )
    return response.text
