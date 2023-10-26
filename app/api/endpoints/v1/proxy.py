from fastapi import HTTPException, Depends, APIRouter
from app.core.config import settings
from app.core.rate_limiter import rate_limiter
from app.api.endpoints.dependencies import get_auth_token
import requests

router = APIRouter()

@router.post("/predict")
def predict(data: dict, token: str = Depends(get_auth_token)):
    """
    Forward the incoming request to the GenHealth Predict API.

    Args:
    - data (dict): A history array containing an ordered sequence of medical events, demographic data, or meta tokens.
    - token (str): The API token for GenHealth, fetched from the environment.

    Returns:
    - dict: Predicted results from the GenHealth API.
    """
    return forward_request(data, settings.GENHEALTH_PREDICT_URL, token)

@router.post("/embeddings")
def embeddings(data: dict, token: str = Depends(get_auth_token)):
    """
    Forward the incoming request to the GenHealth Embeddings API.

    Args:
    - data (dict): A history array containing an ordered sequence of medical events, demographic data, or meta tokens.
    - token (str): The API token for GenHealth, fetched from the environment.

    Returns:
    - dict: Embeddings results from the GenHealth API.
    """
    return forward_request(data, settings.GENHEALTH_EMBEDDINGS_URL, token)

def forward_request(data: dict, url: str, token: str):
    """
    Helper function to forward the request to the specified GenHealth API endpoint.

    Args:
    - data (dict): A history array containing an ordered sequence of medical events, demographic data, or meta tokens.
    - url (str): The GenHealth API endpoint to forward the request to.
    - token (str): The API token for GenHealth.

    Returns:
    - dict: Response from the GenHealth API endpoint.
    """
    if not rate_limiter.is_allowed("proxy"):
        raise HTTPException(status_code=429, detail="Too many requests")

    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()
