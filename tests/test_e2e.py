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
            "title": "viva",
            "description": "scaloni",
        },
    )
    assert response.status_code == 201
    course_data = response.json()["data"]  # Access the "data" object in the POST response
    course_id = course_data["id"]   # Extract the "id" from the "data" object

    assert uuid.UUID(course_id)  
    assert course_data == {"id": course_id, "title": "viva", "description": "scaloni"}

def test_get_courses():
    response = client.post(
        "/courses/",
        json={
            "title": "NeymarJr",
            "description": "es GOD",
        },
    )
    assert response.status_code == 201
    course_data = response.json()["data"]  
    course_id = course_data["id"]  
    response = client.get("/courses/")
    assert response.status_code == 200
    courses = response.json()["data"]  

    # Check if the created course exists in the list of courses
    assert any(
        course["id"] == course_id and course["title"] == "NeymarJr" and course["description"] == "es GOD"
        for course in courses
    )

def test_get_course_by_id():
    response = client.post(
        "/courses/",
        json={
            "title": "AM2",
            "description": "ACERO",
        },
    )
    assert response.status_code == 201
    course_data = response.json()["data"]  
    course_id = course_data["id"]  

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    course_data = response.json()["data"]  

    # Assert the course data matches the expected values
    assert course_data == {"id": course_id, "title": "AM2", "description": "ACERO"}

def test_delete_course_by_id():
    response = client.post(
        "/courses/",
        json={
            "title": "AM2",
            "description": "maulhardtEsGod",
        },
    )
    assert response.status_code == 201
    course_data = response.json()["data"]  
    course_id = course_data["id"]  

    response = client.delete(f"/courses/{course_id}")
    assert response.status_code == 204

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 404