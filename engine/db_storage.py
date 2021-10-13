#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from os import getenv
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
from models.Pot import Pot
from models.User import User
classes = {"User": User, "Pot": Pot}

class DBStorage():
    """Class DBStorage inherit from Base"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ESPot_USER = getenv('ESPot_USER')
        ESPot_PWD = getenv('ESPot_PWD')
        ESPot_HOST = getenv('ESPot_HOST')
        ESPot_DB = getenv('ESPot_DB')
        self.__engine = create_engine('mysql+mysqldb://root:root@localhost/ESPot')

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
