#!/usr/bin/env python3
"""Setting up a basic Babel Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """configure available languages in application"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def hello_world():
    """renders template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
