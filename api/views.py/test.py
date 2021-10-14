#!/usr/bin/python3
""" handles restful api actions """

from flask import Flask, jsonify, abort, request
from api.views import app_views
from models import storage

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users_list = []
    for user in storage.all("User").values():
        users_list.append(user.to_dict())
    return (jsonify(users_list))
