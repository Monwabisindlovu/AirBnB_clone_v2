#!/usr/bin/python3
"""
This script starts a Flask web application with specified routes.
"""

from flask import Flask
from flask import render_template
from flask import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays 'C ', followed by the value of the text variable."""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """Displays 'Python ', followed by the value of the text variable."""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Displays 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page with H1 tag: 'Number: n' if n is an integer."""
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page with H1 tag: 'Number: n is even|odd' if n is an integer."""
    return render_template('6-number_odd_or_even.html', number=n, even_or_odd='even' if n % 2 == 0 else 'odd')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
