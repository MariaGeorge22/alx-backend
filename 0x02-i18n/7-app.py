#!/usr/bin/env python3
""" Module for Second Flask Task """

from typing import Dict, Optional
from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    user = g.user if g is not None else None
    return render_template('7-index.html', user=user)


@babel.localeselector
def get_locale() -> Optional[str]:
    """ determine the best match with our supported languages """
    query_local = request.args.get("locale")
    if query_local in Config.LANGUAGES:
        return query_local
    if g.user is not None:
        user_locale = g.user.get("locale")
        if user_locale in Config.LANGUAGES:
            return user_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_get_timezone() -> Optional[str]:
    """ determine the best match with our supported languages """
    try:
        query_local = request.args.get("get_timezone")
        if query_local is not None:
            return pytz.timezone(query_local).zone
        if g.user is not None:
            user_get_timezone = g.user.get("get_timezone")
            if user_get_timezone is not None:
                return pytz.timezone(user_get_timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    finally:
        return "UTC"


def get_user(login_as: str) -> Optional[Dict[str, str]]:
    """ returns a user dictionary or
    None if the ID cannot be found or
    if login_as was not passed """
    try:
        login_as = int(login_as)
        return users.get(login_as, None)
    except Exception:
        pass


@app.before_request
def before_request():
    """ gets User from query params """
    login_as = request.args.get('login_as')
    g.user = get_user(login_as)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
