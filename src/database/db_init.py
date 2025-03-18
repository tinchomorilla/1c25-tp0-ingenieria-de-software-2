# db_init.py
from src.database.db import engine, Base

def initialize_database():
    Base.metadata.create_all(bind=engine)
