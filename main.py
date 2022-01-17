from easyocr import Reader
from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import run as uvicorn_run


app = FastAPI()


class UrlImage(BaseModel):
    url_img: str


async def process_image(img: str) -> tuple:
    """
    Recognize text (ru/en) in an image.
    :param img: link to img-object
    :return: tuple with recognized text
    """
    reader = Reader(
        ['ru', 'en'],
        gpu=False,
        download_enabled=False,
        model_storage_directory='/app/EasyOCR'
    )
    result: tuple = tuple(reader.readtext(img, detail=0, paragraph=True))
    return result


@app.post('/bot/')
async def root(image_file: UrlImage):
    return await process_image(img=image_file.url_img)
