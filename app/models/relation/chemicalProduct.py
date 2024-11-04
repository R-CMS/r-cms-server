from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db.database import Base


class ChemicalProduct(Base):
    __tablename__ = 'chemical_product'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)

    chemical_id = Column(String, ForeignKey('chemical.cas'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)

    chemical = relationship('Chemical', back_populates='chemicalProducts')
    product = relationship('Product', back_populates='chemicalProducts')
