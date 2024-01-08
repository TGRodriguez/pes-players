from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import os

Engine = None


def create_session():
    DB_DIALECT = os.environ.get("DB_DIALECT")
    DB_HOST = os.environ.get("DB_HOST")
    DB_NAME = os.environ.get("DB_NAME")
    DB_PORT = os.environ.get("DB_PORT")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")

    # Generate Database URL
    DATABASE_URL = f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(DATABASE_URL)

    # Create Database Engine
    Engine = create_engine(DATABASE_URL, echo=False, future=True)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
    return SessionLocal


def get_db_connection():
    db = scoped_session(create_session())
    try:
        yield db
    finally:
        db.close()
