from sqlalchemy import Column, Integer, String
from app.database import Base

class Connection(Base):
    __tablename__ = 'connections'
    id = Column(Integer, primary_key=True)
    ssid = Column(String(256))
    psk = Column(String(256))