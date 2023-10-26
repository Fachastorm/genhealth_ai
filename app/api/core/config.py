from decouple import config

class Settings:
    GENHEALTH_API_TOKEN: str = config("GENHEALTH_API_TOKEN")
    GENHEALTH_PREDICT_URL: str = config("GENHEALTH_PREDICT_URL", default="https://api.genhealth.ai/predict")
    GENHEALTH_EMBEDDINGS_URL: str = config("GENHEALTH_EMBEDDINGS_URL", default="https://api.genhealth.ai/embeddings")

settings = Settings()
