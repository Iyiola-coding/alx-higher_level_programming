#!/usr/bin/python3
""" Write a script that lists all State objects from the database hbtn_0e_6_usa """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(bind=engine)
    
    Base.metadata.create_all(engine)
    
    session = session()
    
    output = session.query(State).order_by(State.id).all()
    for state in output:
        print("{}: {}".format(state.id, state.name))

    session.close()
