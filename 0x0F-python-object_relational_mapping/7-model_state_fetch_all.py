#!/usr/bin/python3
"""
This script lists all state objects from the database hbtn_e_6_usa.

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create an engine and connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name
        ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # Display the resutls
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    # close session
    session.close()
