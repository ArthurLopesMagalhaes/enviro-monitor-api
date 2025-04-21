# models.py
from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from database import Base

class Leitura(Base):
    __tablename__ = "leituras"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
