from fastapi.testclient import TestClient
from src.main import app
from src.database.db import get_db

base_url = "http://web_test:8001"

client = TestClient(app, base_url=base_url)

def test_create_course():
    response = client.post(
        "/courses/",
        json={
            "name": "Hola",
            "description": " GOD",
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "Hola",
        "description": " GOD",
    }