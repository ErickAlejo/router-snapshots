from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from typing import Any

def init_connection_to_db(path_db:str) -> Any:
    engine = create_engine(f"sqlite:///{path_db}", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    return session