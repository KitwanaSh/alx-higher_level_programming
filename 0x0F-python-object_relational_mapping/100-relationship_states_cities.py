#!/usr/bin/python3
""" Insert a state with its city """

import sys
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_100_usa")
    Base.metadata.create_all(engine)

    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    session.add(City(name="San Fransisco", state=State(name="California")))
    session.commit()
    session.close()
