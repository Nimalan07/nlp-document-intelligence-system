from pydantic import BaseModel
class ExtractionResponse(BaseModel):
    extracted_entities: dict