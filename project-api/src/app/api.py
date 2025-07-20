from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    api_key: Optional[str] = None
    db_url: str = "sqlite:///./test.db"
    debug: bool = False
    app_name: str = "FastAPI 應用程式1"


class HealthResponse(BaseModel):
    status: str
    app_name: str
    debug: bool


settings = Settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!", "app_name": settings.app_name}


@app.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="healthy", app_name=settings.app_name, debug=settings.debug
    )


@app.get("/settings")
def get_settings():
    # 不要在回應中暴露敏感資訊如 api_key
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "db_url": settings.db_url if not settings.api_key else "***隱藏***",
    }
