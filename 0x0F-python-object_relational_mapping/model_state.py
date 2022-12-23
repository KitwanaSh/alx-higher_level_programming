#!/usr/bin/python3
""" Using sqlachemy """

from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ Makes the state enhrit the code """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
