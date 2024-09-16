#!/usr/bin/env python3
"""flask app with parameterized template"""
from flask import Flask, render_template, request, g
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


def get_user():
    """ returns a user dictionary or
        None if ID not found or login_as not passed
    """
    user_id = request.args.get("login_as")
    if user_id:
        user_id = int(user_id)
        if user_id in users:
            return users.get(user_id)
    return None


@app.before_request
def before_request():
    """ use get_user to find a user if any,
        and set it as a global on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ use a user’s preferred local if it is supported.
        The order of priority should be:
            - Locale from URL parameters
            - Locale from user settings
            - Locale from request header
            - Default locale
    """
    locale = request.args.get('locale')
    if locale is None and g.user is not None:
        locale = g.user.get('locale')

    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """renders template"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
