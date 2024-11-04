from sqlalchemy import Column, Integer, Double, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db.database import Base


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    volume = Column(Double, nullable=False)
    safe_quantity = Column(Integer, nullable=False)

    storage_id = Column(Integer, ForeignKey('storage.id'), nullable=False)

    storage= relationship('Storage', back_populates='inventory')
    histories = relationship('History', back_populates='inventory')
