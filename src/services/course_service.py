from sqlalchemy.orm import Session
from repositories.course_repository import create_course, get_courses, get_course_by_id
from schemas.course_schemas import CourseBase
from models.course_model import Course

# Service to create a course
def create_new_course(db: Session, course: CourseBase) -> Course:
    return create_course(db=db, course=course)

# Service to get all courses
def get_all_courses(db: Session):
    return get_courses(db=db)

# Service to get a course by ID
def get_course_by_id_service(db: Session, course_id: int):
    return get_course_by_id(db=db, course_id=course_id)
