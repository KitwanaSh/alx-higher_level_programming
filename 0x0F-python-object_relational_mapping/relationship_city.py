#!/usr/bin/python3
""" Simple city object class """

from lib2to3.pytree import Base
from sqlalchemy.ext.declarative import declarative_base
from sre_parse import State
from sqlalchemy import String, Column, Integer, ForeignKey, null
Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
