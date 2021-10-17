#!/usr/bin/python3
"""
Contains class Plant
"""
from sqlalchemy import Column, String, SmallInteger, Boolean
from sqlalchemy.sql.schema import ForeignKey
from models.BaseModel import Base, BaseModel


class Plant(BaseModel, Base):
    """Creation of our object Plant"""
    __tablename__ = 'plant'
    Plant_name = Column(String(30), nullable=False, unique=True)
    Humidity_irrigation = Column(SmallInteger, nullable=False, default=70)
    
    def __init__(self, *args, **kwargs):
        """initializes Pot"""
        super().__init__(*args, **kwargs)
