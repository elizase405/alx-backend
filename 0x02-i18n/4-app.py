#!/usr/bin/env python3
"""flask app with parameterized template"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@app.route('/')
def hello_world():
    """renders template"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
