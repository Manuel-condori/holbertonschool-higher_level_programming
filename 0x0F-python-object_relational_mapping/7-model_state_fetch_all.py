#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(argv) != 4:
        print("Error")
    else:
        USER = argv[1]
        PASS = argv[2]
        DATAB = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(USER, PASS, DATAB), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        for instance in session.query(State).order_by(State.id):
            print("{}: {}".format(instance.id, instance.name))
