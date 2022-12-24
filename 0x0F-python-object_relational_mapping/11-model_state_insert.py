#!/usr/bin/python3
""" Add a new object to the state
    Args:
        - user: The database user
        - passwd: The user password
        - db: the actual database
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from unicodedata import name

if __name__ == "__main__":
    """
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_6_usa")
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    new_loui = State(name="Louisiana")
    session.add(new_loui)
    session.commit()
    print(new_loui.id)
