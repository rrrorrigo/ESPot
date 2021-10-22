#!/usr/bin/python3
"""
runs flask application
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from models import *
from models import storage
from models.Pot import Pot
from models.User import User
from models.Plant import Plant
from hashlib import md5
from flask_cors import CORS
app = Flask(__name__)
app.config['SECRET_KEY'] = md5("peñarol".encode()).hexdigest()
CORS(app)


@app.route('/my_plants/<string:user_id>', strict_slashes=False)
def my_plants(user_id=""):
    """plant of user"""
    usr = storage.get(User, user_id)
    all_pots = usr.Pots
    pot = storage.get(Pot, all_pots[0].id)
    plants = storage.all(Plant).values()
    plants = sorted(plants, key=lambda k: k.Plant_name)
    return render_template('/my_plants.html', pot=pot, plants=plants)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        pwd = request.form['password']
        check = storage.getByAttribute(User, username)
        if check:
            print("entro al chekc")
            if md5(pwd.encode()).hexdigest() == check.password:
                user_id = storage.getByAttribute(User, username).id
                return redirect(url_for("my_plants", user_id=user_id))
            print("contrasena incorrecta")
        flash(u"Invalid login credentials", "error")
        return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        if storage.getByAttribute(User, name) or storage.getByAttribute(User, email):
            flash(u"User already exists", "error")
            return redirect(url_for('register'))
        new_user = User(username=name, email=email, password=pwd)
        new_user.save()
        return redirect(url_for('login'))


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True)
