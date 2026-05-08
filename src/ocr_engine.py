import cv2
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
class OCREngine:
    def __init__(self):
        pass

    def preprocess_image(self, image):
        if not isinstance(image, Image.Image):
            image = Image.open(image)
        image = np.array(image)
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        resized = cv2.resize(gray,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
        denoised = cv2.fastNlMeansDenoising(resized)
        threshold = cv2.adaptiveThreshold(denoised,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        return threshold

    def extract_text(self, image):
        processed_image = self.preprocess_image(image)
        text = pytesseract.image_to_string(processed_image, config="--oem 3 --psm 6" )
        return text.strip()