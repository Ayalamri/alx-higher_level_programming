#!/usr/bin/python3
"""Adds the State California with the City San Francisco to the database
hbtn_0e_100_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    california = State(name='California')

    # Create a new City object
    san_francisco = City(name='San Francisco')

    # Add the city to the state's list of cities
    california.cities.append(san_francisco)

    # Add the state to the session
    session.add(california)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
