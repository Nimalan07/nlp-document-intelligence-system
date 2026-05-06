import os

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from api.schemas import ExtractionResponse
from src.inference_pipeline import InferencePipeline


router = APIRouter()


@router.post("/extract", response_model=ExtractionResponse)
async def extract_entities(file: UploadFile = File(...)):
    upload_path = f"data/raw/{file.filename}"

    with open(upload_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    pipeline = InferencePipeline(upload_path)

    extracted_entities = pipeline.run_pipeline()

    os.remove(upload_path)

    return {
        "extracted_entities": extracted_entities
    }