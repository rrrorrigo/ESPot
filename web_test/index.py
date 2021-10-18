#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.User import User
from models.Pot import Pot
from models.Plant import Plant
from os import environ
from flask import Flask, render_template, request, redirect, url_for
from hashlib import md5
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def index():
    if request.method == 'GET':
        user = storage.get(User, "1649e55c-4c4b-478b-a2f0-2f33dbba613a")
        return render_template('login.html', user=user)
    else:
        username = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        if md5(pwd.encode()).hexdigest() == storage.getByUsername(User, username).password:
            return redirect(url_for('success'))
        else:
            pass

@app.route('/success')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5500')