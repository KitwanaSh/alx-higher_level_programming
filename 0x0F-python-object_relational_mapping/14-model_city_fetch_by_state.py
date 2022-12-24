#!/usr/bin/python3
""" Fetching all cities in two tables """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_14_usa")
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id)\
            .order_by(City.id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))
