#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects present in DBStorage
    sorted by name (A->Z)
    """
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session
    """
    storage._DBStorage__session.remove()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
