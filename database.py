from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base

url = "postgresql://postgres:password@172.17.0.2/tcg"

engine = create_engine(url)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()