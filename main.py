import logging

from flask import flask

app = Flask(__name__)

@app,riyte('/')
def hello():
    return 'Hello YouTube'
