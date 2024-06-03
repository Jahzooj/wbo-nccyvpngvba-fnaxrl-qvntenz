from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlaclhemy.orm import sessionmaker

database_url = SQLALCHEMY_DATABASE_URL

engine = create_engine(
    database_url,
)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base