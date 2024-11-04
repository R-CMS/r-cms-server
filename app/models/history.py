from datetime import datetime

from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db.database import Base
from app.models.enum.histype import HisType


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    type = Column(Enum(HisType), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    created_by = Column(Integer, ForeignKey('user.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    expendable_id = Column(Integer, ForeignKey('expendable.id'), nullable=False)

    created_user = relationship('User', back_populates='histories')
    inventory = relationship('Inventory', back_populates='histories')
    expendable = relationship('Expendable', back_populates='histories')
