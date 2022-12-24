#!/usr/bin/python3
""" 
the city model
"""

from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import Column, String, Integer

class City(Base):
    """ The City inherits from 'Base'"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)
