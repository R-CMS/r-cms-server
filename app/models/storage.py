from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db.database import Base


class Storage(Base):
    __tablename__ = 'storage'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    inventory = relationship("Inventory", back_populates="storage")
    expendables = relationship("Expendable", back_populates="storage")
