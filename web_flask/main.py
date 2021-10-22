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
    pot = storage.get(Pot, "10fe8791-7ab2-4302-8848-b0a6d280ae48")
    plants = storage.all(Plant)
    return render_template('/my_plants.html', pot=pot, plants=plants)


@app.route('/my_plants/test/<string:user_id>', strict_slashes=False)
def my_plants_test(user_id=""):
    """plant of user"""
    usr = storage.get(User, user_id)
    pot = storage.get(Pot, "10fe8791-7ab2-4302-8848-b0a6d280ae48")
    return render_template('/test_real_time_data.html', pot=pot)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        pwd = request.form['password']
        check = storage.getByAttribute(User, username)
        if check:
            if md5(pwd.encode()).hexdigest() == check.password:
                user_id = storage.getByAttribute(User, username).id
                return redirect(url_for("my_plants", user_id=user_id))
        flash(u"Invalid login credentials", "error")
        return redirect(url_for('login'))


""" 
@app.route('/login', strict_slashes=False)
def login():
    
    
    return render_template('index.html', states=states, state_id=state_id)
"""

@app.route('/register', strict_slashes=False)
def register():
    
    
    return render_template('register.html')

"""
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
