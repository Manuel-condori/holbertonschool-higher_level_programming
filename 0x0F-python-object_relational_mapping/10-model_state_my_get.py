#!/usr/bin/python3
"""
script that prints the State
object with the name passed as
argument from the
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(argv) != 5:
        print("Error")
    else:
        USER = argv[1]
        PASS = argv[2]
        DATAB = argv[3]
        STATE = argv[4]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(USER, PASS, DATAB), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name == STATE).first()
        if state is None:
            print("Not found")
        else:
            print(state.id)
