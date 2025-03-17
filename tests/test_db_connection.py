from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Database URL
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

def test_db_connection():
    try:
        # Create the engine and try to connect
        engine = create_engine(DATABASE_URL)
        # Connect to the database (this will throw an exception if connection fails)
        with engine.connect() as connection:
            print("Database connection successful!")
    except OperationalError as e:
        print(f"Error: Could not connect to the database. {e}")

if __name__ == "__main__":
    test_db_connection()
