from sqlalchemy import Column, Integer, String, Text
from db.models import Base

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(String(200))
    preferences = Column(Text)
    loyalty_points = Column(Integer, default=0)

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"