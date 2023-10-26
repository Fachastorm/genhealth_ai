from fastapi import FastAPI
from app.api.endpoints.v1 import proxy

app = FastAPI()

app.include_router(proxy.router, prefix="/v1")
