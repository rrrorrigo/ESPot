#!/usr/bin/python3
"""
Contains class User
"""
from sqlalchemy import Column, String
from uuid import uuid4
from sqlalchemy.orm import relationship
from engine.db_storage import Base


class User(Base):
    """Creation of our object User"""
    __tablename__ = 'user'
    id_user = Column(String(60), nullable=False, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    email = Column(String(320), nullable=False)
    Pots = relationship('Pot', cascade="all, delete", backref="User")

    def ___init__(self, *arg):
        """Initalize method that asign unique id to User object"""
        self.id_user = str(uuid4())

    def __repr__(self):
        return "<id = {}(username = {}, password = {}, email = {}, Pots {})>"