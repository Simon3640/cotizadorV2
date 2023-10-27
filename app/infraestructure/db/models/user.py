from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

if TYPE_CHECKING:
    from .sale import Sale



class User(BaseModel):
    email = Column(String(100), unique=True)
    names = Column(String(100), nullable=True)
    last_names = Column(String(100), nullable=True)
    identification = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    hashed_password = Column(String(300), nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    active = Column(Boolean, nullable=True, default=True)

    sales = relationship("Sale", back_populates="user")
