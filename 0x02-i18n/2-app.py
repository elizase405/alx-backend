#!/usr/bin/env python3
"""Flask app"""
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


@bable.localeselector
def get_locale():
    """returns the languages that best matches our application"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """renders template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
