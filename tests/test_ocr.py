from PIL import Image

from src.ocr_engine import OCREngine


def test_extract_text():
    image = Image.open("sample_documents/form_sample.png")

    ocr_engine = OCREngine()

    text = ocr_engine.extract_text(image)

    assert isinstance(text, str)
    assert len(text) > 0