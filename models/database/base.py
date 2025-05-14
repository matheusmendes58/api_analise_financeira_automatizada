# Database connection configuration

from core.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

ENGINE_ALCHEMY = create_engine(settings.connect_db, echo=False)
DBSESSION = scoped_session(sessionmaker(bind=ENGINE_ALCHEMY, expire_on_commit=False))
SESSION =  scoped_session(sessionmaker(bind=ENGINE_ALCHEMY))
BASE = declarative_base()

def create_table():
    """
        Create table in database.
        However, if it has already been created, it can be used as a connection test.

        :return: None
        """
    pass
