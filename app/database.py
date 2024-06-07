from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

database_url = DATABASE_URL

try:
    engine = create_engine(
        database_url,
    )

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
except Exception as e:
    print(f'connection failed: {e}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()