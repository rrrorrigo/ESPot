#!/usr/bin/python3
"""
runs flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
from models.Pot import Pot
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/home/<string:pot_id>', strict_slashes=False)
def home(pot_id=""):
    """testing"""
    pot = storage.get(Pot, pot_id)
    return render_template('index.html', pot=pot)


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
