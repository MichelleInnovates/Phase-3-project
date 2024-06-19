from sqlalchemy import Column, Integer, String, Text, Boolean
from db.models import Base
from sqlalchemy.orm import declarative_base
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

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}', address='{self.address}')>"