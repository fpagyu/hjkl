# coding: utf-8
from hjkl import app

from flask import jsonify


@app.route('/hjkl/index')
def index():
    return jsonify(msg="Hello, Flask!")
