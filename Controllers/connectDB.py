from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Connect:

    engine = create_engine("postgresql://postgres:postgres@localhost:5432/Python_bot")
    Base = declarative_base()

    _instace = None

    def __new__(cls, *args, **kwargs):
        if not cls._instace:
            cls._instace = super().__new__(cls, *args, **kwargs)
        return cls._instace

    def __init__(self):
        pass

    def saveDataCurrency(self, data):
        sessionMaker = sessionmaker(Connect.engine)
        session = sessionMaker()

        try:
            session.add_all(data)
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()


































































