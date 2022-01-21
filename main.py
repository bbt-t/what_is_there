from logging import getLogger

from fastapi import FastAPI
from pydantic import BaseModel

from easyocr_path.easyocr_main import process_image


logger = getLogger('__name__')
app = FastAPI()


class UrlImage(BaseModel):
    imageurl: str


@app.post('/bot-ocr/')
async def root(incoming_info: UrlImage) -> tuple:
    """
    Accept image-url for processing
    :param incoming_info: post-data (json)
    :return: result in tuple
    """
    return await process_image(img=incoming_info.imageurl)
