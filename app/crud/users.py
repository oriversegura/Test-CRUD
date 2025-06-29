from database import engine 
from sqlalchemy.exc import OperationalError
from sqlalchemy import text

def test_db_conection(engine):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successfull!")
        return True
    except OperationalError as e:
        print(f"Database conection failed: {e}")
        return False
    
    if test_db_conection(engine):
        print("Continue app running process")
    else: 
        print("App cant continue running")
