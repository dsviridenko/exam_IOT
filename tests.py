import pytest
from fastapi.testclient import TestClient
from main import app
from app.api.v1.web import items_db

client = TestClient(app)


def test_read_root_pass():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


def test_read_root_fail():
    response = client.get("/invalid")
    assert response.status_code == 404


def test_read_items_pass():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_read_items_fail():
    # Нет сценария FAIL для этого эндпоинта
    pass


def test_read_item_pass():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_read_item_fail():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_create_item_pass():
    data = {"name": "NewItem", "price": 15.99}
    response = client.post("/items", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "NewItem"


def test_create_item_fail():
    data = {"price": 15.99}  # Отсутствует обязательное поле 'name'
    response = client.post("/items", json=data)
    assert response.status_code == 422
    assert "name" in response.text  # Проверка наличия ошибки в ответе


def test_delete_item_pass():
    client.post("/items?name=TempItem")
    temp_id = len(items_db)

    response = client.delete(f"/items/{temp_id}")
    assert response.status_code == 204

    response = client.get(f"/items/{temp_id}")
    assert response.status_code == 404


def test_delete_item_fail():
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]