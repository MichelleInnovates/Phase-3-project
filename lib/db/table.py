from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models import Base

class Table(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    table_number = Column(String(20), nullable=False)
    seating_capacity = Column(Integer)
    table_type = Column(String(50))
    available = Column(Boolean, default=True)

    restaurant = relationship("Restaurant", backref="tables")

    def __repr__(self):
        return f"<Table(id={self.id}, restaurant_id={self.restaurant_id}, table_number='{self.table_number}')>"