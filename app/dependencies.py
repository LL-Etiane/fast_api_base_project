from database.db import SessionLocal

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()