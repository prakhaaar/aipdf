from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db.database import Base

class PDF(Base):
    __tablename__ = "pdfs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    filepath = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)