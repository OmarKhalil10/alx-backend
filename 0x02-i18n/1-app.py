#!/usr/bin/env python3
""" a basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    """ render a basic html file """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
