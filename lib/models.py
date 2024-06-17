from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    reservations = relationship('Reservation', backref='customer')

class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    capacity = Column(Integer)
    reservations = relationship('Reservation', backref='table')

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    date_time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)
