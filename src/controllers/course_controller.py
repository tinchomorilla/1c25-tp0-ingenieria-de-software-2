from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.course_service import create_new_course, get_all_courses, get_course_by_id_service
from schemas.course_schemas import CourseBase, Course
from database.db import get_db

router = APIRouter()

# Create a new course (POST request)
@router.post("/", response_model=Course)
def create_course(course: CourseBase, db: Session = Depends(get_db)):
    return create_new_course(db=db, course=course)

# Get all courses (GET request)
@router.get("/", response_model=list[Course])
def get_courses(db: Session = Depends(get_db)):
    return get_all_courses(db=db)


# Get a course by ID (GET request)
@router.get("/{id}", response_model=Course)
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    return get_course_by_id_service(db=db, course_id=course_id)
