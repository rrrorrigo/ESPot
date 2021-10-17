#!/usr/bin/python3
"""
Contains class User
"""
from sqlalchemy import Column, String, SmallInteger, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.BaseModel import Base, BaseModel
from models.Plant import Plant


class Pot(BaseModel, Base):
    """Creation of our object User"""
    __tablename__ = 'pot'
    Actual_humidity = Column(SmallInteger, default=0)
    Is_empty = Column(Boolean, nullable=False, default=1)
    Last_irrigation = Column(String(10), default="N/A", nullable=False)
    Username = Column(String(30), ForeignKey('user.username'))
    Turned_ON = Column(Boolean, nullable=False, default=False) # fichate si hice todo bien ******************

    def __init__(self, *args, **kwargs):
        """initializes Pot"""
        super().__init__(*args, **kwargs)
