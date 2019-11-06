from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base
from sqlalchemy.orm import relationship

class Hall(Base):
    __tablename__ = 'halls'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    hall_id = Column(Integer,ForeignKey('halls.id'))
    students=relationship("Halls",back_populates="students")
