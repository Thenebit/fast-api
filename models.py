# This acts as the table for the sqlite application
from database import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
