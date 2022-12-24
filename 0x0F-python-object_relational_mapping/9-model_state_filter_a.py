#!/usr/bin/python3
""" This list State that contains the letter 'a' in the database
    Args():
        - User: The username
        - passwrd: the password
        - db = the database (here, we are using the mysqlalchemy
"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_6_usa")
    """
    engine = create_engine("mysql.mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    
    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    for state in session.query(State).order_by(State.id).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
