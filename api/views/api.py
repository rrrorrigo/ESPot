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


@app_views.route('/user_pots/<string:user_id>', methods=['GET'], strict_slashes=False)
def get_user_pots(user_id):
    usr = storage.get(User, user_id)
    print(usr.Pots)
    return jsonify(usr.Pots)


@app_views.route('/pots', methods=['GET', 'POST'], strict_slashes=False)
def get_pots():
    if request.method == 'GET':
            all_pots = storage.all(Pot).values()
            list_pots = []
            for pot in all_pots:
                list_pots.append(pot.to_dict())
            return jsonify(list_pots)
    else:
        data = request.get_json()
        dictionary = {}
        for k, v in data:
            dictionary[k] = v
        pot = Pot(**dictionary)
        pot.save()
        return jsonify(pot.to_dict())


@app_views.route('/selected/<string:id_usr>', methods=['GET', 'PUT'], strict_slashes=False)
def selected_web(id_usr):
    """Api that be updated by WebPage"""
    if request.method == 'GET':
        usr = storage.get(User, id_usr)
        pot = storage.get(Pot, usr.Pots[0].id)
        rlist = []
        rlist.append(pot.to_dict())
        rlist.append(storage.get(Plant, pot.Plant_id).to_dict())
        return jsonify(rlist)
    else:
        print("antes del form")
        data = request.get_json()
        print(data)
        if not data:
            abort(400, "Not a JSON")
        usr = storage.get(User, id_usr)
        pot = storage.get(Pot, usr.Pots[0].id)
        plant = storage.getByAttribute(Plant, data['Plant_name'])
        setattr(pot, 'Plant_id', plant.id)
        pot.save()
        return jsonify(storage.get(Pot, pot.id).to_dict())


@app_views.route('/get_humidity/<string:id_pot>', methods=['GET'], strict_slashes=False)
def set_humidity(id_pot):
    """The arduino will make a request to know the wanted level of humidity"""
    to_esp = {}
    pot = storage.get(Pot, id_pot)
    plant = storage.get(Plant, pot.Plant_id)
    to_esp["Humidity_irrigation"] = str(plant.Humidity_irrigation)
    to_esp["Turned_ON"] =  pot.Turned_ON
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
    if "irrigated" in data and data["irrigated"] == "True":
        setattr(pot, "Last_irrigation", now)
    if "Is_empty" in data and data["Is_empty"]:
        setattr(pot, "Is_empty", bool(eval(data["Is_empty"])))
    if "Actual_humidity" in data and data["Actual_humidity"]:
        setattr(pot, "Actual_humidity", int(float(data["Actual_humidity"])))
    if "Turned_ON" in data:
        setattr(pot, "Turned_ON", data["Turned_ON"])
    pot.save()
    return (jsonify({"culo": "Peñarol"}), 200)
