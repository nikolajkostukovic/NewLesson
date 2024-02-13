import datetime
import uuid

from sqlalchemy import create_engine, Column, String, MetaData, UUID, Text, text, \
    DateTime, VARCHAR, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

engine = create_engine("postgresql://postgres:postgres@localhost:5432/Python_bot")

Base = declarative_base()
metadata = MetaData()

class Currency(Base):
    __tablename__ = 'currency'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    numCode = Column(Text) # 826
    charCode =  Column(Text) # GBP
    nominal =  Column(Integer) # 1
    name = Column(Text) # Фунт
    value = Column(Float) # 43, 8254
    vunitRate = Column(Float)# 43, 8254
    date = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, numCode, charCode, nominal, name, value, vunitRate):
        self.numCode = numCode
        self.charCode = charCode
        self.nominal = nominal
        self.name = name
        self.value = value
        self.vunitRate = vunitRate
        self.id = uuid.uuid4()
        self.date = datetime.datetime.now()