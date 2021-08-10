#!/usr/bin/python3
"""
script that prints all City objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
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

        for city, state in session.query(City, State) \
                                  .filter(City.state_id == State.id) \
                                  .order_by(City.id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
