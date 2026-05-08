from fastapi import FastAPI
from api.routes import router
app = FastAPI(
    title="NLP Document Intelligence System",
    version="1.0.0"
)
app.include_router(router)