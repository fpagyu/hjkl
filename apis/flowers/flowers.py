# coding: utf-8
from flask import request, jsonify
from werkzeug.utils import secure_filename

from apps import app


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


@app.route("/flowers/login")
def login():
    # 获取微信openid进行登录, 进入小程序即登录
    pass


@app.route("/flowers/orders")
def get_orders():
    # 获取用户订单列表
    pass


@app.route("/flowers/orders/<order_id>")
def get_order_detail():
    # 获取订单详情
    pass


@app.route("/flowers/orders")
def post_order():
    # 提交订单
    pass


@app.route("/flowers/orders")
def put_order():
    # 修改订单状态
    pass


@app.route("/flowers/banner")
def flowers_banner():
    # 获取banner数据
    pass


@app.route("/flowers/filter")
def goods_filter():
    # 根据分类获取商品列表
    pass


@app.route("/flowers/goods")
def post_goods():
    # 编辑商品
    pass

