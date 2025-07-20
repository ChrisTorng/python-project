from fastapi.testclient import TestClient
from app.api import app, settings, Point

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


def test_point_dataclass():
    """測試 Point dataclass 的基本功能"""
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2
    assert str(point) == "Point(x=1, y=2)"


def test_create_point_get():
    """測試透過 GET 建立 Point"""
    response = client.get("/point/3/4")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["point"]["x"] == 3
    assert json_response["point"]["y"] == 4
    assert json_response["point"]["representation"] == "Point(x=3, y=4)"
    assert json_response["distance_from_origin"] == 5.0  # 3-4-5 三角形


def test_create_point_post():
    """測試透過 POST 建立 Point"""
    response = client.post("/point", json={"x": 5, "y": 12})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["point"]["x"] == 5
    assert json_response["point"]["y"] == 12
    assert json_response["point"]["representation"] == "Point(x=5, y=12)"
    assert json_response["distance_from_origin"] == 13.0  # 5-12-13 三角形


def test_create_point_post_default_values():
    """測試 POST 請求預設值"""
    response = client.post("/point", json={})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["point"]["x"] == 0
    assert json_response["point"]["y"] == 0
    assert json_response["point"]["representation"] == "Point(x=0, y=0)"
    assert json_response["distance_from_origin"] == 0.0
