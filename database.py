from psycopg2 import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base import Base
from models.tcg import CardSets, Cards

url = "postgresql://postgres:password@172.17.0.2/tcg"

try:
    engine = create_engine(url)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    Base.metadata.create_all(engine)
except OperationalError as e:
    print(e)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()