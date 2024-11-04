from sqlalchemy import String, Column, Float, Enum, LargeBinary
from sqlalchemy.orm import relationship

from app.core.db.database import Base
from app.models.enum.classification import Classification
from app.models.enum.unit import Unit


class Chemical(Base):
    __tablename__ = 'chemical'

    cas = Column(String, primary_key=True, index=True)
    ko_name = Column(String, unique=True, nullable=True)
    en_name = Column(String, unique=True, nullable=True)
    molecular_formula = Column(String, nullable=True)
    description = Column(String, nullable=True)
    chemical_law = Column(LargeBinary, nullable=True)
    risk_coefficient = Column(Float, nullable=True)
    specified_quantity = Column(Float, nullable=True)
    health_type = Column(Enum(Classification), nullable=True)
    density = Column(Float, nullable=True)
    units = Column(Enum(Unit), nullable=False)

    chemicalProducts = relationship("ChemicalProduct", back_populates="chemical")
