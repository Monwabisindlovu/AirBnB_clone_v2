#!/usr/bin/python3
"""
This module defines a simple Flask web application with a route that
displays "Hello HBNB!" when accessed.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
