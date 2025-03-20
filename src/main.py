import os
import uvicorn
from fastapi import FastAPI
from src.controllers.course_controller import router as courses_router
from src.database.db_init import initialize_database
from src.errors.exception_handler import configure_exception_handlers
from src.controllers.health_check import router as health_router


app = FastAPI()

# Initialize the database (create tables if they don't exist)
initialize_database()

# Include Health check endpoint
app.include_router(health_router, tags=["health"])

# Include Courses router
app.include_router(courses_router, prefix="/courses", tags=["courses"])

# Register custom exception handlers
configure_exception_handlers(app)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))