from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from settings import DATABASE_URL

Base = declarative_base()

_engine = create_engine(DATABASE_URL) # type: ignore
_SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=_engine
)

def get_db():
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
