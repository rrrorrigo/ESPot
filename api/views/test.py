#!/usr/bin/python3
""" handles restful api actions """

from flask import Flask, jsonify, abort, request
from api import views
from api.views import app_views
from models import storage
from datetime import datetime
from pytz import timezone

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

@app_views.route('/send_humidity', methods=['POST'], strict_slashes=False)
def humidity():
    actual_humidity = request.get_json()
    if not actual_humidity:
        abort(400, 'Not a JSON')
    now = datetime.now(timezone("Etc/GMT-3")).strftime("%d/%m %H:%M")
    now = str(now)
    response = {}
    response["Humidity"] = actual_humidity.get("humidity")
    response["time"] = now
    return jsonify(response)