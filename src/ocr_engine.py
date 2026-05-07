import cv2
import numpy as np
import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCREngine:
    def __init__(self):
        pass

    def preprocess_image(self, image):
        if not isinstance(image, Image.Image):
            image = Image.open(image)

        image = np.array(image)

        if len(image.shape) == 3:
            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

        else:
            gray = image

        threshold = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        return threshold

    def extract_text(self, image):
        processed_image = self.preprocess_image(image)

        text = pytesseract.image_to_string(
            processed_image,
            config="--oem 3 --psm 6"
        )

        return text.strip()