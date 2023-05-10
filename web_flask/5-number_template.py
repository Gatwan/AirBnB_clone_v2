#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Function called with / route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Function called with /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Function called with /c/<text> route"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """Function called with /python/(<text>) route"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """Function called with /number/<n> route"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """Function called with /number_template/<n> route"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
