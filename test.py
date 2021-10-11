#!/usr/bin/python3
"""testing models"""
from models import User


userTest = User()
userTest.name = "Rigoberto"
userTest.password = "123"
userTest.email = "holbertonschool@gmail.com"
print(userTest)