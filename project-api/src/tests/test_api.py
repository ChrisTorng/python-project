from fastapi.testclient import TestClient
from app.api import app, settings

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["message"] == "Hello, FastAPI!"
    assert json_response["app_name"] == settings.app_name


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "healthy"
    assert "app_name" in json_response
    assert "debug" in json_response


def test_get_settings():
    response = client.get("/settings")
    assert response.status_code == 200
    json_response = response.json()
    assert "app_name" in json_response
    assert "debug" in json_response
    assert "db_url" in json_response
    # 確保沒有暴露敏感資訊
    assert "api_key" not in json_response
