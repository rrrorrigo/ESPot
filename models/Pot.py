#!/usr/bin/python3
"""
Contains class User
"""
from sqlalchemy import Column, String, SmallInteger, Boolean
from uuid import uuid4
from sqlalchemy.sql.schema import ForeignKey
from engine.db_storage import Base


class Pot(Base):
    """Creation of our object User"""
    __tablename__ = 'pot'
    id_ESP = Column(String(60), nullable=False, primary_key=True)
    Plant_name = Column(String(30), nullable=False, unique=True)
    Humidity_irrigation = Column(SmallInteger, nullable=False)
    Is_empty = Column(Boolean, nullable=False, default=1)
    username = Column(String(30), ForeignKey('user.username'))

    def ___init__(self, *arg):
        """Initalize method that asign unique id to Pot object"""
        self.id_ESP = str(uuid4())