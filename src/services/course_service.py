import uuid
from sqlalchemy.orm import Session
from src.repositories.course_repository import (
    db_create_course,
    db_delete_course_by_id,
    db_get_courses,
    db_get_course_by_id,
)
from src.schemas.course import CourseBase, Course


# Service to create a course
def create_new_course(db: Session, course: CourseBase) -> Course:
    return db_create_course(db=db, course=course)


# Service to get all courses
def get_all_courses(db: Session):
    return db_get_courses(db=db)


# Service to get a course by ID
def get_course_by_id_service(db: Session, course_id: uuid.UUID):
    return db_get_course_by_id(db=db, course_id=course_id)

def delete_course_by_id_service(db: Session, course_id: uuid.UUID):
    return db_delete_course_by_id(db=db, course_id=course_id)