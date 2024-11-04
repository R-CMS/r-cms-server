from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.core.db.database import Base
from app.models.enum.role import Role


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(Role), default=Role.USER, nullable=False)

    histories = relationship('History', back_populates='created_user')
    inspections = relationship('Inspection', back_populates='user')
