from asyncio import get_running_loop
from concurrent.futures import ProcessPoolExecutor
from logging import getLogger

from fastapi import FastAPI
from pydantic import BaseModel

from easyocr_path.easyocr_main import process_image


logger = getLogger('__name__')
app = FastAPI()


async def cpu_bound_run_func(func, *args):
    loop = get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func, *args)
    return result


class UrlImage(BaseModel):
    imageurl: str


@app.post('/bot-ocr/')
async def root(incoming_info: UrlImage) -> tuple:
    """
    Accept image-url for processing
    :param incoming_info: post-data (json)
    :return: result in tuple
    """
    return await cpu_bound_run_func(process_image, incoming_info.imageurl)
