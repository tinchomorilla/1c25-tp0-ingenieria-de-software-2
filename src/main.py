import os
import uvicorn
from fastapi import FastAPI
from src.database.db_init import initialize_database
from src.errors.exception_handler import configure_exception_handlers
from src.router.routes import router as api_router

app = FastAPI()

# Initialize the database (create tables if they don't exist)
initialize_database()

# Include the API router
app.include_router(api_router)

# Register custom exception handlers
configure_exception_handlers(app)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))