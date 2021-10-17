#!/usr/bin/python3
""" handles restful api actions """

from flask import jsonify, abort, request
from api.views import app_views
from models import storage
from datetime import datetime
from pytz import timezone
from models.Pot import Pot
from models.User import User
from models.Plant import Plant

@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def get_users():
    """Api to check login on Front-End"""
    if request.method == 'GET':
        users_list = {}
        for user in storage.all("User").values():
            users_list[user.username] = user.id
        return jsonify(users_list)
    else:
        data = request.get_json()
        dictionary = {}
        for k, v in data:
            dictionary[k] = v
        user = User


@app_views.route('/pots', methods=['GET', 'POST'], strict_slashes=False)
def get_pots():
    users_list = {}
    for user in storage.all("User").values():
        users_list[user.username] = user.id
    return jsonify(users_list)


@app_views.route('/selected/<string:id_pot>', methods=['GET', 'POST'], strict_slashes=False)
def selected_web(id_pot):
    """Api that be updated by WebPage"""
    if request.method == 'GET':
        return jsonify(storage.get(Pot, id_pot))
    else:
        data = request.get_json()
        if not data:
            abort(400, "Not a JSON")
        if not data['id']:
            abort(400, 'Missing id')
        key = Pot + '.' + data['id']
        setattr(storage.all()[key], 'Humidity_irrigation', data['Humidity_irrigation'])
        setattr(storage.all()[key], 'Last_irrigation', data['Last_irrigation'])
        storage.all()[key].save()
        return jsonify(storage.get(Pot, id_pot))


@app_views.route('/get_humidity/<string:id_pot>', methods=['GET'], strict_slashes=False)
def set_humidity(id_pot):
    """The arduino will make a request to know the wanted level of humidity"""
    to_esp = {}
    pot = storage.get(Pot, id_pot)
    plant = storage.get(Plant, pot.Plant_id)
    to_esp["Humidity_irrigation"] = str(plant.Humidity_irrigation)
    to_esp["Turned_ON"] =  "True" #str(pot.Turned_ON)
    return(jsonify(to_esp))


@app_views.route('/send_data/<string:id_pot>', methods=['PUT'], strict_slashes=False)
def send_data(id_pot):
    """Update pot data - water level, humidity, time of last irrigation"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    now = datetime.now(timezone("America/Montevideo")).strftime("%d/%m %H:%M")
    now = str(now)
    pot = storage.get(Pot, id_pot)
    if data["irrigated"] == "True":
        setattr(pot, "Last_irrigation", now)
    setattr(pot, "Is_empty", bool(eval(data["Is_empty"])))
    setattr(pot, "Actual_humidity", int(float(data["Actual_humidity"])))
    storage.save()
    return (jsonify(pot.to_dict()), 200)
