from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import get_db_url

engine = create_engine(get_db_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)