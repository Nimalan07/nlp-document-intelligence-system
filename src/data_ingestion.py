from pathlib import Path

from pdf2image import convert_from_path
from PIL import Image


class DataIngestion:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_image(self):
        image = Image.open(self.file_path)
        return image

    def load_pdf(self):
        pages = convert_from_path(self.file_path)
        return pages

    def load_text(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    def load_document(self):
        suffix = self.file_path.suffix.lower()

        if suffix in [".png", ".jpg", ".jpeg"]:
            return self.load_image()

        if suffix == ".pdf":
            return self.load_pdf()

        if suffix == ".txt":
            return self.load_text()

        raise ValueError("Unsupported file format")