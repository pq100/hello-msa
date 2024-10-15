from datetime import datetime

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    pno = Column(Integer, primary_key=True,
                 autoincrement=True, index=True)
    name = Column(String(18), nullable=False)
    desc = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    maker = Column(String(50), nullable=False)
    regdate = Column(String(20), nullable=False)