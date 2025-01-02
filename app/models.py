from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Good(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    manufacturer = Column(String)
    distributor = Column(String)
    retailer = Column(String)
    consumer = Column(String)
    timestamp = Column(DateTime)