#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    # connect to the server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create a session representing a transaction with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Find the State object with id=2
    state = session.query(State).filter_by(id=2).first()
    # Update the name
    state.name = "New Mexico"
    session.commit()

    session.close()
