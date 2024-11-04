from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.core.db.database import Base


class Expendable(Base):
    __tablename__ = 'expendable'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    safe_quantity = Column(Integer, nullable=False)

    storage_id = Column(Integer, ForeignKey('storage.id'), nullable=False)

    storage = relationship("Storage", back_populates="expendables")
    histories = relationship("History", back_populates="expendable")