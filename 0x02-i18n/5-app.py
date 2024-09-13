#!/usr/bin/env python3
"""flask app with parameterized template"""
from flask import Flask, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# configure available languages in application
class Config:
    """configure available languages in application"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ detect if the incoming request contains locale argument and
        ifs value is a supported locale, return it.
        If not or if the parameter is not present,
        resort to the previous default behavior.
    """
    locale = request.args.get('locale')

    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary if ID not found or login_as not passed """
    login_as = request.args.get('login_as')

    if ID:
        return users[ID]
    else if login_as:
        return users[login_as]


@app.route('/')
def hello_world():
    """renders template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
