from PIL import Image

from src.ocr_engine import OCREngine
from src.preprocess import TextPreprocessor
from src.entity_extraction import EntityExtractor
from src.post_processing import PostProcessor

from src.key_value_extraction import (
    KeyValueExtractor
)
class InferencePipeline:
    def __init__(self, document_path):
        self.document_path = document_path

        self.ocr_engine = OCREngine()

        self.preprocessor = TextPreprocessor()

        self.entity_extractor = EntityExtractor()

        self.post_processor = PostProcessor()

        self.key_value_extractor = KeyValueExtractor()

    def run_pipeline(self):
        document = Image.open(
            self.document_path
        )

        text = self.ocr_engine.extract_text(
            document
        )

        cleaned_text = (
            self.preprocessor.clean_text(
                text
            )
        )

        entities = (
            self.entity_extractor.extract_entities(
                cleaned_text
            )
        )

        cleaned_entities = (
            self.post_processor.clean_entities(
                entities
            )
        )

        structured_output = ( self.key_value_extractor.extract_pairs(cleaned_entities)
)
        return structured_output