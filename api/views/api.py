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
        all_users = storage.all(User).values()
        list_users = []
        for user in all_users:
            list_users.append(user.to_dict())
        return jsonify(list_users)
    else:
        data = request.get_json()
        dictionary = {}
        for k, v in data:
            dictionary[k] = v
        user = User(**dictionary)
        user.save()
        return jsonify(user.to_dict())

@app_views.route('/plants', methods=['GET', 'POST'], strict_slashes=False)
def get_plants():
    if request.method == 'GET':
        all_plants = storage.all(Plant).values()
        list_plants = []
        for plant in all_plants:
            list_plants.append(plant.to_dict())
        return jsonify(list_plants)
    else:
        data = request.get_json()
        dictionary = {}
        for k, v in data:
            dictionary[k] = v
        plant = Plant(**dictionary)
        plant.save()
        return jsonify(plant.to_dict())


@app_views.route('/pots', methods=['GET', 'POST'], strict_slashes=False)
def get_pots():
    if request.method == 'GET':
            all_pots = storage.all(Pot).values()
            list_pots = []
            for pot in all_pots:
                list_pots.append(pot.to_dict())
            return jsonify(all_pots) #hardcoded
    else:
        data = request.get_json()
        dictionary = {}
        for k, v in data:
            dictionary[k] = v
        pot = Pot(**dictionary)
        pot.save()
        return jsonify(pot.to_dict())


@app_views.route('/selected/<string:id_pot>/<string:id_plant>', methods=['GET', 'POST'], strict_slashes=False)
def selected_web(id_pot, id_plant):
    """Api that be updated by WebPage"""
    if request.method == 'GET':
        pot = storage.get(Pot, id_pot)
        plant = storage.get(Plant, id_plant)
        dictionary = {}
        dictionary['Pot'] = pot.to_dict()
        dictionary['Plant'] = plant.to_dict()
        return jsonify(dictionary)
    else:
        data = request.get_json()
        if not data:
            abort(400, "Not a JSON")
        if not data['id']:
            abort(400, 'Missing id')
        keyPlant = Plant + '.' + data['Plant']['id']
        keyPot = Pot + '.' + data['Pot']['id']
        setattr(storage.all()[keyPlant], 'Plant_name', data['Plant']['Plant_name'])
        setattr(storage.all()[keyPlant], 'Humidity_irrigation', data['Plant']['Humidity_irrigation'])
        setattr(storage.all()[keyPot], 'Last_irrigation', data['Pot']['Last_irrigation'])
        setattr(storage.all()[keyPot], 'Turned_ON', data['Pot']['Turned_ON'])
        storage.all()[keyPlant].save()
        storage.all()[keyPot].save()
        return jsonify(storage.get(Pot, id_pot))


@app_views.route('/get_humidity/<string:id_pot>', methods=['GET'], strict_slashes=False)
def set_humidity(id_pot):
    """The arduino will make a request to know the wanted level of humidity"""
    to_esp = {}
    pot = storage.get(Pot, id_pot)
    plant = storage.get(Plant, pot.Plant_id)
    to_esp["Humidity_irrigation"] = str(plant.Humidity_irrigation)
    to_esp["Turned_ON"] =  "True" #str(pot.Turned_ON) ************************* NO OLVIDARSE DESCOMENTAR ESTO DESPue *********
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
    if data["Is_empty"]:
        setattr(pot, "Is_empty", bool(eval(data["Is_empty"])))
    if data["Actual_humidity"]:
        setattr(pot, "Actual_humidity", int(float(data["Actual_humidity"])))
    if data["Turned_ON"]:
        setattr(pot, "Turned_ON", bool(eval(data["Turned_ON"])))
    storage.save()
    return (jsonify({"culo": "Peñarol"}), 200)
