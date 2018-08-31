# coding: utf-8
from hjkl import app

from flask import jsonify


@app.route('/hjkl')
def index():
    return jsonify(msg="Hello, Flask!")
