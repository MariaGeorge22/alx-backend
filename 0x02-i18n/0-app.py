#!/usr/bin/env python3
""" Module for first Flask Task """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_route() -> str:
    """simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>)"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
