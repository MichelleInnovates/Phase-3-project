from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    # Add more attributes as needed

class Table(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    table_number = Column(String(20), nullable=False)
    seating_capacity = Column(Integer)


class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    reservation_time = Column(DateTime, nullable=False)
    

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    