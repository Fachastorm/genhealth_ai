from fastapi import HTTPException, Depends, APIRouter
from app.core.config import settings
from app.core.rate_limiter import rate_limiter
import requests

router = APIRouter()

def get_auth_token():
    return settings.GENHEALTH_API_TOKEN

@router.post("/predict")
def predict(data: dict, token: str = Depends(get_auth_token)):
    return forward_request(data, settings.GENHEALTH_PREDICT_URL, token)

@router.post("/embeddings")
def embeddings(data: dict, token: str = Depends(get_auth_token)):
    return forward_request(data, settings.GENHEALTH_EMBEDDINGS_URL, token)

def forward_request(data: dict, url: str, token: str):
    if not rate_limiter.is_allowed("proxy"):
        raise HTTPException(status_code=429, detail="Too many requests")

    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()
