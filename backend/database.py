from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from utils.config import settings

engine = create_engine(settings.database_url)

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

class Base(DeclarativeBase):

    pass

def get_db():

    db = sessionLocal()

    try:

        yield db

    finally:

        db.close()
