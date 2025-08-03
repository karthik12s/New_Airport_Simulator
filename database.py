import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = os.getenv("db_conn_string", "postgresql://postgres:postgres@localhost:5432/airport_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
db_session = scoped_session(SessionLocal)

Base = declarative_base()
Base.query = db_session.query_property()
