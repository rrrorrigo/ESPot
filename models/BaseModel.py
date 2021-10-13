#!/usr/bin/python3
"""This module defines a base class for all Objects"""
import uuid
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)

    def __init__(self, *args, **kwargs):
        """Method that initialize the object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """String representation of its object"""
        return "<[ {} ] ( {} )>".format(self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """delete the current instance from the storage
        (models.storage) by calling the method delete"""
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        return dictionary