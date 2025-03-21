import uuid
from fastapi.testclient import TestClient
from src.main import app
from src.database.db import get_db

base_url = "http://web_test:8001"

client = TestClient(app, base_url=base_url)

def test_create_course():
    response = client.post(
        "/courses/",
        json={
            "name": "viva",
            "description": "scaloni",
        },
    )
    assert response.status_code == 201
    course_id = response.json()["id"]
    assert uuid.UUID(course_id)
    assert response.json() == {"id": course_id, "name": "viva", "description": "scaloni"}

def test_get_courses():
    response = client.post(
        "/courses/",
        json={
            "name": "NeymarJr",
            "description": "es GOD",
        },
    )
    course_id = response.json()["id"]
    response = client.get("/courses/")
    assert response.status_code == 200
    courses = response.json()
    assert any(course["id"] == course_id and course["name"] == "NeymarJr" and course["description"] == "es GOD" for course in courses)

def test_get_course_by_id():
    response = client.post(
        "/courses/",
        json={
            "name": "AM2",
            "description": "ACERO",
        },
    )
    course_id = response.json()["id"]
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == {"id": course_id, "name": "AM2", "description": "ACERO"}

def test_delete_course_by_id():
    response = client.post(
        "/courses/",
        json={
            "name": "AM2",
            "description": "maulhardtEsGod",
        },
    )
    course_id = response.json()["id"]
    response = client.delete(f"/courses/{course_id}")
    assert response.status_code == 204
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 404