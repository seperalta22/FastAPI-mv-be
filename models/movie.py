from re import S
from config.database import Base
from sqlalchemy import Column, Integer, ARRAY, String


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    casts = Column(String)
    genres = Column(String)
