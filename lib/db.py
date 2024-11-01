from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///task_manager.db"
Base = declarative_base()

def get_engine():
    return create_engine(DATABASE_URL)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
