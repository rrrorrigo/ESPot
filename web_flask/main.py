#!/usr/bin/python3
"""
runs flask application
"""

from flask import Flask, render_template, request, redirect, url_for
from models import *
from models import storage
from models.Pot import Pot
from models.User import User
from hashlib import md5
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/<user_id>/my_plants', strict_slashes=False)
def home(user_id=""):
    """testing"""
    usr = storage.get(User, user_id)
    return render_template('/my_plants.html')

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def index():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        pwd = request.form['password']
        if md5(pwd.encode()).hexdigest() == storage.getByUsername(User, username).password:
            user_id = storage.getByUsername(User, username).id
            return redirect(url_for("my_plants", user_id=user_id))
        else:
            pass


""" 
@app.route('/login', strict_slashes=False)
def login():
    
    
    return render_template('index.html', states=states, state_id=state_id)


@app.route('/register', strict_slashes=False)
def register():
    
    
    return render_template('index.html', states=states, state_id=state_id)


@app.route('/page', strict_slashes=False)
def page():
    
    
    return render_template('index.html', states=states, state_id=state_id)
 """

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True)
