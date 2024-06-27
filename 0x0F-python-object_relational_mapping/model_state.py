#!/usr/bin/python3

"""
This is a script that contains the class definition of a state and
an instance Base = declarative_base()

"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    State class that links to the mysql table states

    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
