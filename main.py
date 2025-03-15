from fastapi import FastAPI
from api.courses import router as courses_router  
from api.users import router as users_router

app = FastAPI()

app.include_router(courses_router, prefix="/courses", tags=["courses"])
#app.include_router(users_router, prefix="/users", tags=["users"])
