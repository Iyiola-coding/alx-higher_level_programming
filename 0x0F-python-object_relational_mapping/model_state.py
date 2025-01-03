#!/usr/bin/python3
""" Write a python file that contains the class definition of a State and an
instance Base = declarative_base(): """
import sys
from model_state import Base, State

from SQLAlchemy import (create_engine)

if __name__ == "__main__":
    engine = create_enine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
    Base.metadata.create_all(engine)
