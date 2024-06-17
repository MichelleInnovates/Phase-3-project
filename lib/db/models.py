from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    email = Column(String(100))
    website = Column(String(100))
    description = Column(Text)
    active = Column(Boolean, default=True)

class Table(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    table_number = Column(String(20), nullable=False)
    seating_capacity = Column(Integer)
    table_type = Column(String(50))  # e.g., indoor, outdoor, booth, etc.
    available = Column(Boolean, default=True)

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    reservation_time = Column(DateTime, nullable=False)
    party_size = Column(Integer)
    special_requests = Column(Text)
    confirmed = Column(Boolean, default=False)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(String(200))
    preferences = Column(Text)
    loyalty_points = Column(Integer, default=0)