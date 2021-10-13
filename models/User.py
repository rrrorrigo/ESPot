#!/usr/bin/python3
"""
Contains class User
"""
from hashlib import md5
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.BaseModel import Base, BaseModel


class User(BaseModel, Base):
    """Creation of our object User"""
    __tablename__ = 'user'
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    email = Column(String(320), nullable=False)
    Pots = relationship('Pot', cascade="all, delete", backref="Owner")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
