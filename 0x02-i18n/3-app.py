#!/usr/bin/env python3
""" Module for Second Flask Task """

from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """a Config class that has a LANGUAGES class attribute
    equal to ["en", "fr"]"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home_route() -> str:
    """simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>)
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """ determine the best match with our supported languages """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
