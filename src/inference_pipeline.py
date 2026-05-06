from src.data_ingestion import DataIngestion
from src.entity_extraction import EntityExtractor
from src.ocr_engine import OCREngine
from src.post_processing import PostProcessor
from src.preprocess import TextPreprocessor


class InferencePipeline:
    def __init__(self, file_path):
        self.file_path = file_path

        self.data_ingestion = DataIngestion(file_path)
        self.ocr_engine = OCREngine()
        self.preprocessor = TextPreprocessor()
        self.entity_extractor = EntityExtractor()
        self.post_processor = PostProcessor()

    def run_pipeline(self):
        document = self.data_ingestion.load_document()

        if isinstance(document, list):
            text = ""

            for page in document:
                extracted_text = self.ocr_engine.extract_text(page)
                text += extracted_text + " "

        elif isinstance(document, str):
            text = document

        else:
            text = self.ocr_engine.extract_text(document)

        cleaned_text = self.preprocessor.clean_text(text)

        entities = self.entity_extractor.extract_entities(cleaned_text)

        processed_entities = self.post_processor.process_entities(
            entities
        )

        return processed_entities