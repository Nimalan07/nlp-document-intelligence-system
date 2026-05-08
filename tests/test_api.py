from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)
def test_extract_api():
    with open("sample_documents/form_sample.png", "rb") as file:
        response = client.post(
            "/extract",
            files={"file": ("form_sample.png", file,"image/png" )})
    assert response.status_code == 200