#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    mysql_name = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

# connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_name, mysql_password, database_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

# query the database for all State objects and print the results
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}:{}".format(state.id, state.name))

    session.close()
