from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.course_model import Course as DBCourse
from src.schemas.course import CourseBase


# Create a course in the database
def db_create_course(db: Session, course: CourseBase):
    db_course = DBCourse(name=course.name, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


# Get all courses from the database
def db_get_courses(db: Session):
    return db.query(DBCourse).all()


# Get a course by ID
def db_get_course_by_id(db: Session, course_id: int):
    return db.query(DBCourse).filter(DBCourse.id == course_id).first()

# Delete a course by ID
def db_delete_course_by_id(db: Session, course_id: int):
    course = db.query(DBCourse).filter(DBCourse.id == course_id).first()
    if not course:
        return None
    db.delete(course)
    db.commit()
    return course
