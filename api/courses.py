from fastapi import APIRouter
from models.course_models import Course

router = APIRouter()

@router.post("/")
def create_course(course: Course):
    return {"name": course.name, "description": course.description}



