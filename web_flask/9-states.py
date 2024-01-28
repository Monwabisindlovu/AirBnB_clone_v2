#!/usr/bin/python3
"""Script that starts a Flask web application."""

from flask import render_template
from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id=None):
    """Display states and cities."""
    states = storage.all(State)
    state = None
    
    if id:
        state_id = 'State.' + id
        state = states.get(state_id)

    return render_template('9-states.html', states=states, state=state)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
