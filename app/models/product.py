from sqlalchemy import Column, Integer, Enum, String, LargeBinary
from sqlalchemy.orm import relationship

from app.core.db.database import Base
from app.models.enum.classification import Classification


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(Classification), nullable=False)
    company = Column(String, nullable=False)
    name = Column(String, nullable=False)
    msds = Column(String, nullable=False)
    description = Column(String, nullable=False)
    ghs_sign = Column(LargeBinary, nullable=False)
    inventory_id = Column(Integer, nullable=False)

    chemicalProducts = relationship("ChemicalProduct", back_populates="product")
