# coding: utf-8
from flask import request, jsonify
from werkzeug.utils import secure_filename

from apps import app

from apps.flowers.services.flowers import FlowerService


@app.route("/flowers/testing")
def testing():
    if request.method == "GET":
        # "?username="   request.args.get
        username = request.args.get('username')
        session_id = request.cookies.get('sessionid', '')

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # file upload
        f = request.files['the_file']
        f.save('/tmp/' + secure_filename(f.filename))

    return "aaaa"


@app.route("/flowers/<int:flower_id>")
def get_flower(flower_id):
    flower = FlowerService.get_by_pk(flower_id)
    if flower is None:
        return jsonify({
            'ok': False,
            'code': 4004,
            'msg': 'not found'
        })

    data = {
        'id': flower.id,
        'name': flower.name,
        'path': flower.path,
        'content': flower.content
    }

    return jsonify({
        'ok': True,
        'data': data
    })
