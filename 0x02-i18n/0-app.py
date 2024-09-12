#!/usr/bin/env python3
"""Setting up a basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)

# render html template on / route
@app.route('/')
def hello_world():
    """renders template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
