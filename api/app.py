#!/usr/bin/python3
""" app.py """

from api.views import app_views
from flask_cors import CORS
from flask import Flask, jsonify
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def remove_sesh(self):
    '''remove the current SQLAlchemy Session after request'''
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    '''404 page not found handler'''
    err = {"error": "Not found"}
    return (jsonify(**err), 404)

if __name__ == "__main__":
    h = '0.0.0.0'
    p = 5000
    app.run(host=h, port=p, threaded=True)
