from sqlalchemy.orm import Session
from models.course_model import Course as DBCourse  
from schemas.course_schemas import CourseBase  

# Create a course in the database
def create_course(db: Session, course: CourseBase):
    db_course = DBCourse(name=course.name, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)  
    return db_course

# Get all courses from the database
def get_courses(db: Session):
    return db.query(DBCourse).all()  

# Get a course by ID
def get_course_by_id(db: Session, course_id: int):
    return db.query(DBCourse).filter(DBCourse.id == course_id).first()
