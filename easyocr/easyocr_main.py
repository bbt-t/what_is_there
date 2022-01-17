from easyocr import Reader


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