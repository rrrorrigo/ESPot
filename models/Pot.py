#!/usr/bin/python3
"""
Contains class User
"""
from sqlalchemy import Column, String, SmallInteger, Boolean
from sqlalchemy.sql.schema import ForeignKey
from models.BaseModel import Base, BaseModel


class Pot(BaseModel, Base):
    """Creation of our object User"""
    __tablename__ = 'pot'
    Plant_name = Column(String(30), nullable=False, unique=True)
    Humidity_irrigation = Column(SmallInteger, nullable=False)
    Is_empty = Column(Boolean, nullable=False, default=1)
    username = Column(String(30), ForeignKey('user.username'))

    def __init__(self, *args, **kwargs):
        """initializes Pot"""
        super().__init__(*args, **kwargs)