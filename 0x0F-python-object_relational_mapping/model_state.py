#!/usr/bin/python3
"""preparing to Start using the ORM in python """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """The Database module using ORM"""

    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
