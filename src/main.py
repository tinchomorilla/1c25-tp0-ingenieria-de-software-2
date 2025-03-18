from fastapi import FastAPI
from src.controllers.course_controller import router as courses_router
from src.database.db_init import initialize_database
from src.errors.exception_handler import configure_exception_handlers


app = FastAPI()

# Initialize the database (create tables if they don't exist)
initialize_database()

app.include_router(courses_router, prefix="/courses", tags=["courses"])


# Register custom exception handlers
configure_exception_handlers(app)