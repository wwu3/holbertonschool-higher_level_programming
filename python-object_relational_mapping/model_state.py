#!/usr/bin/python3
"""
model_state contains the State class
and Base = declarative_base()
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    db_uri = ("mysql+mysqldb://root@localhost:3306/hbtn_0e_6_usa")
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
