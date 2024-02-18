#!/usr/bin/python3

"""
This script starts a Flask web application with specific routes.
"""

from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns the message 'Hello HBNB!'."""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the message 'HBNB'."""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Returns 'C ' followed by the value of the text variable."""
    text = unquote(text.replace("_", " "))
    return ("C {}").format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Returns 'Python ' followed by the value of the text variable."""
    text = unquote(text.replace("_", " ")) if text else 'is cool'
    return ("Python {}").format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000  debug=None)

