from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True)
    student = Column(String)
    course = Column(String)
    issuer = Column(String)
    cert_hash = Column(String, unique=True)
    issued_at = Column(DateTime, default=datetime.utcnow)
