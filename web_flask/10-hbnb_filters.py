#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page with filters"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
