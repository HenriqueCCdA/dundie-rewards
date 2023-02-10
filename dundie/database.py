import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine

from dundie import models  # IMPORTAANTE!!!
from dundie.settings import SQL_CON_STRING

warnings.filterwarnings("ignore", category=SAWarning)

engine = create_engine(SQL_CON_STRING, echo=False)
models.SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    return Session(engine)
