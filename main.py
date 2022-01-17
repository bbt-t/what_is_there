from fastapi import FastAPI
from pydantic import BaseModel

from config import req_easyocr
from easyocr.easyocr_main import process_image


app = FastAPI()


class UrlImage(BaseModel):
    url_img: str


@app.post(req_easyocr)
async def root(image_file: UrlImage):
    return await process_image(img=image_file.url_img)
