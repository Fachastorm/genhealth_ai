import os
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

# Fetch the API key from the environment variables
# API_KEY = os.environ.get("GENHEALTH_API_TOKEN")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Token {settings.GENHEALTH_API_TOKEN}",
}

def test_predict_endpoint():
    """
    Test the predict endpoint of the proxy API.
    
    This test sends a realistic patient history to the predict endpoint 
    and checks that the response contains predictions from the GenHealth API.
    """
    
    # Sample data for the test representing a patient's medical history.
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
    
    # Send the request to the predict endpoint.
    response = client.post("/v1/predict", headers=headers, json=data)
    
    # Assert that the response status is 200 (OK) and contains predictions.
    assert response.status_code == 200
    assert "predictions" in response.json()

def test_embeddings_endpoint():
    """
    Test the embeddings endpoint of the proxy API.
    
    This test sends a realistic patient history to the embeddings endpoint 
    and checks that the response contains embeddings from the GenHealth API.
    """
    
    # Sample data for the test representing a patient's medical history.
    data = {
        "history": [
            {"code": "64", "system": "age", "display": "64"},
            {"code": "E11", "system": "ICD10CM", "display": "Type 2 diabetes mellitus"},
            {"code": "E11.3551", "system": "ICD10CM", "display": "Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye"}
        ]
    }
    
    # Send the request to the embeddings endpoint.
    response = client.post("/v1/embeddings", headers=headers, json=data)
    
    # Assert that the response status is 200 (OK) and contains embeddings.
    assert response.status_code == 200
    assert "embedding" in response.json()
