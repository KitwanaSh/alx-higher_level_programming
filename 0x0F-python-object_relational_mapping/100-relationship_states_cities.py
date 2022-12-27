#!/usr/bin/python3
""" Insert a state with its city """

import sys
from unicodedata import name
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_100_usa")
    """
    Base.metadata.create_all(engine)

    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    session.add(City(name="San Fransisco", state=State(name="California")))
    session.commit()
    session.close()
