from easyocr import Reader

from main import logger


def process_image(img: str) -> tuple | None:
    """
    Recognize text (ru/en) in an image.
    :param img: link to img-object
    :return: tuple with recognized text
    """
    try:
        reader = Reader(
            ['ru', 'en'],
            gpu=False,
            download_enabled=False,
            model_storage_directory='/app/EasyOCR'
        )
        result = tuple(reader.readtext(str(img), detail=0, paragraph=True))
    except BaseException as err:
        logger.critical(f'--- {repr(err)} ---')

    return result
