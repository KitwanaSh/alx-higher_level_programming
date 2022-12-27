#!/usr/bin/python3
""" The state of country """


from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from relationship_city import Base, City

Base = declarative_base()

class State(Base):
    """ Inheritance from Base
    declarative
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
