from sqlalchemy import Column, Integer, String, DateTime
import datetime
from app.models.base import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    deleted_at = Column(DateTime, nullable=True)