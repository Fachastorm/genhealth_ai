from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    data = {
        "history": [
            {"code": "64", "system": "age", "display": "64"},
            {"code": "E11", "system": "ICD10CM", "display": "Type 2 diabetes mellitus"},
            {"code": "E11.3551", "system": "ICD10CM", "display": "Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye"}
        ],
        "num_predictions": 1,
        "generation_length": 10,
        "inference_threshold": 0.95,
        "inference_temperature": 0.95
    }
    response = client.post("/v1/predict", json=data)
    assert response.status_code == 200
    assert "predictions" in response.json()

def test_embeddings_endpoint():
    data = {
        "history": [
            {"code": "64", "system": "age", "display": "64"},
            {"code": "E11", "system": "ICD10CM", "display": "Type 2 diabetes mellitus"},
            {"code": "E11.3551", "system": "ICD10CM", "display": "Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye"}
        ]
    }
    response = client.post("/v1/embeddings", json=data)
    assert response.status_code == 200
    assert "embedding" in response.json()
