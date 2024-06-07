from sqlalchemy import Column, Boolean, Integer, String, JSON, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    company = Column(String)
    position = Column(String)
    type = Column(String)
    salary_lower = Column(Integer)
    salary_upper = Column(Integer)
    technical_skills = Column(JSON)
    summary = Column(String)
    other_app_info = Column(JSON)
    is_active = Column(Boolean)
    status = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


