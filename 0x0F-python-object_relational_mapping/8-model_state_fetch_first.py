#!/usr/bin/python3
""" Showing the first state object form the database
    Args():
        - user : the uner name
        - passwd: the user password
        - db : the database (here, we are using sqlalchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_6_usa")
    """

    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing/n")
    else:
        print("{}: {}".format(state.id, state.name))
