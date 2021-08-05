from sqlalchemy import (
    Column,
    Integer,
    String
)
from src.config.database import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(60), nullable=False)
    password = Column(String(30), nullable=False)
