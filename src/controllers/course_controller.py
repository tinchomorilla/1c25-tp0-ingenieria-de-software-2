from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.course_service import create_new_course, get_all_courses, get_course_by_id_service
from src.schemas.course import CourseBase, Course
from src.database.db import get_db
from src.schemas.error import ErrorResponse

router = APIRouter()

# Create a new course (POST request)
@router.post("/", status_code=201,
             responses={
                201: {"description": "Course created successfully", "model": Course},
                400: {"description": "Bad response error", "model": ErrorResponse},
            })
def create_course(course: CourseBase, db: Session = Depends(get_db)):
    return create_new_course(db=db, course=course)

# Get all courses (GET request)
@router.get("/", response_model=list[Course], responses={
                200: {"description": "A list of courses", "model": list[Course]},
            })
def get_courses(db: Session = Depends(get_db)):
    return get_all_courses(db=db)


# Get a course by ID (GET request)
@router.get("/{id}", 
            responses={
                200: {"description": "Course retrieved successfully", "model": Course},
                404: {"description": "Course not found", "model": ErrorResponse},
                500: {"description": "Internal server error", "model": ErrorResponse}
            })
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    course = get_course_by_id_service(db=db, course_id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail=f"The course with ID {course_id} was not found.",
            headers={"X-Error": "Course Not Found"}
        )
    return course