from sqlalchemy import Column, DateTime, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db.database import Base


class Inspection(Base):
    __tablename__ = 'inspection'

    date = Column(DateTime, primary_key=True)
    is_complete = Column(Boolean, default=False, nullable=False)
    description = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User', back_populates='inspections')
