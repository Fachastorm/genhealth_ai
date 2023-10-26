from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/v1/predict", json={"key": "value"})
    assert response.status_code == 200
    # Add more assertions based on expected behavior

def test_embeddings_endpoint():
    response = client.post("/v1/embeddings", json={"key": "value"})
    assert response.status_code == 200
    # Add more assertions based on expected behavior
