from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from db.models import Base

class Reservation(Base):
    

    __tablename__ = 'reservations'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    reservation_time = Column(DateTime, nullable=False)
    party_size = Column(Integer)
    special_requests = Column(Text)
    confirmed = Column(Boolean, default=False)

    restaurant = relationship("Restaurant", backref="reservations")
    table = relationship("Table", backref="reservations")
    customer = relationship("Customer", backref="reservations")

    def __repr__(self):
        return f"<Reservation(id={self.id}, restaurant_id={self.restaurant_id}, reservation_time='{self.reservation_time}')>"