import os
from unittest.mock import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  # ??
from sqlalchemy.ext.declarative import declarative_base


sqlite_db_name = "../db.sqlite3"
base_dir = os.path.dirname(os.path.realpath(__file__))

db_url = f"sqlite:///{base_dir}/{sqlite_db_name}"

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
