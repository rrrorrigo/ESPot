#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()