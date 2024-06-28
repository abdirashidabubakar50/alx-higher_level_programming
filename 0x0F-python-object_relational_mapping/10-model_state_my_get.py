#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa

"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:33306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
