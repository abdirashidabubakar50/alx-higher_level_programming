#!/usr/bin/python3
"""
This is a script that prints all City objects from the database hbtn_0e_14_usa

"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    cities = session.query(City, State).filter(
            State.id == City.state_id)

    for c in cities:
        print("{}: ({}) {}".format(c.State.name, c.City.id, c.City.name))

    session.close()
