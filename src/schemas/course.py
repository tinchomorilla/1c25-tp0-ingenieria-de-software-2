import uuid
from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    description: str


# Pydantic model for returning the course data with ID
class Course(CourseBase):
    id: uuid.UUID

    class Config:
        from_attributes = (
            True  # Tells Pydantic to treat the SQLAlchemy model as a dictionary
        )
