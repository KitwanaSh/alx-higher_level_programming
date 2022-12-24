#!/usr/bin/python3
""" Update the State object based on id
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://root:DriverP$996@localhost/hbtn_0e_6_usa")

    session_mk = sessionmaker(bind=engine)
    session = session_mk()

    up_state = session.query(State).filter_by(id=2).first()
    up_state.name = "New Mexico"
    session.commit()
