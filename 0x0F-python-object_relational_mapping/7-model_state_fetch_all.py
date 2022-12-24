#!/usr/bin/python3
""" List all state objects from the database
    Args()
        - user: The username of a sql
        - passwd: The password for the user
        - db: The actual database
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_6_usa")
    """
    
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3],
                pool_pre_ping=True))

    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
