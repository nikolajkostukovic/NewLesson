from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost:5432/Python_bot")
Base = declarative_base()

class Connect:

    def __init__(self):
        pass

    def saveDataCurrency(self, data):
        sessionMaker = sessionmaker(engine)
        session = sessionMaker()

        for item in data:
            session.add(item)




































































