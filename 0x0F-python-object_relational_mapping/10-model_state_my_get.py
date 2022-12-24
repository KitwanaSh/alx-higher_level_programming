#!/usr/bin/python3
""" Use print the id of the state objec based on
their specific state name
    Args():
        - user: The username of the database
        - passwd: the user password in the mysql
        - db: the actual database
        - state_name: The state name to search
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_6_usa")
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
