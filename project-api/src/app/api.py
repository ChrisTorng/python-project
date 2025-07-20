from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from pydantic_settings import BaseSettings
from typing import Optional
from dataclasses import dataclass


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    api_key: Optional[str] = None
    db_url: str = "sqlite:///./test.db"
    debug: bool = False
    app_name: str = "FastAPI 應用程式"


@dataclass
class Point:
    x: int
    y: int


class HealthResponse(BaseModel):
    status: str
    app_name: str
    debug: bool


class PointResponse(BaseModel):
    point: dict
    distance_from_origin: float


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


@app.get("/point/{x}/{y}", response_model=PointResponse)
def create_point(x: int, y: int):
    """建立一個 Point 物件並回傳其資訊"""
    point = Point(x, y)
    distance = (x * x + y * y) ** 0.5
    return PointResponse(
        point={"x": point.x, "y": point.y, "representation": str(point)},
        distance_from_origin=distance,
    )


@app.post("/point", response_model=PointResponse)
def create_point_from_body(point_data: dict):
    """從請求體建立 Point 物件"""
    x = point_data.get("x", 0)
    y = point_data.get("y", 0)
    point = Point(x, y)
    distance = (x * x + y * y) ** 0.5
    return PointResponse(
        point={"x": point.x, "y": point.y, "representation": str(point)},
        distance_from_origin=distance,
    )
