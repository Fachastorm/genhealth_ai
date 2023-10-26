from fastapi import HTTPException
from app.core.config import settings

def get_auth_token():
    if not settings.GENHEALTH_API_TOKEN:
        raise HTTPException(status_code=403, detail="API token not configured")
    return settings.GENHEALTH_API_TOKEN
