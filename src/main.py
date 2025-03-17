# main.py
from fastapi import FastAPI
from controllers.course_controller import router as courses_router
from database.db_init import initialize_database

app = FastAPI()

# Initialize the database (create tables if they don't exist)
initialize_database()

app.include_router(courses_router, prefix="/courses", tags=["courses"])
