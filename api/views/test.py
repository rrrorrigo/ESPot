#!/usr/bin/python3
""" handles restful api actions """

from flask import Flask, jsonify, abort, request
from api.views import app_views
from models import storage

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users_list = {}
    for user in storage.all("User").values():
        users_list[user.username] = user.id

    return jsonify(users_list)
    #users_list = jsonify(users_list)
    #print(type(users_list))
    #return jsonify({})
    #return (users_list)
