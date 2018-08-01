# coding: utf-8
from sqlalchemy import Column, Integer, String, SmallInteger, BigInteger, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    # 用户表

    __tablename__ = 'ft_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String)


class Address(Base):
    # 收货地址

    __tablename__ = 'ft_address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    username = Column(String)
    phone = Column(String)  # 收货人姓名
    address = Column(String)   # 收货地址
    last_at = Column(BigInteger)  # 上一次使用改地址的时间
    is_delete = Column(SmallInteger)


class Order(Base):
    # 订单记录

    __tablename__ = 'ft_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    pay_status = Column(SmallInteger)  # 订单支付状态
    status = Column(SmallInteger)   # 订单状态(0: 订单提交; 1: 接受订单; 2: 关闭订单; 3: 订单完成)
    reason = Column(String)         # 订单关闭原因
    pay_way = Column(SmallInteger)  # 支付方式(微信, 支付宝, 现金支付/当面付款)
    total = Column(Float)           # 订单实付金额
    # discount = Column(Float)        # 优惠金额
    address_id = Column(Integer)    # 收货地址
    create_at = Column(BigInteger)  # 订单创建时间
    update_at = Column(BigInteger)  # 上一次更新时间
    is_delete = Column(SmallInteger)


class OrderGoods(Base):
    # 订单商品

    __tablename__ = 'ft_order_goods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    goods_id = Column(Integer)  # 商品id
    name = Column(String)   # 商品名称
    price = Column(Float)   # 商品实际价格
    market_price = Column(Float)  # 商品原价/市场价
    pic = Column(String)    # 商品图片


class Goods(Base):
    # 商品

    __tablename__ = 'ft_goods'

    id = Column(String, primary_key=True)
    cate_id = Column(Integer)  # 商品分类(花艺, 甜品, 节日)
    name = Column(String)   # 商品名称
    pic = Column(String)    # 商品封面
    detail = Column(String) # 商品规格
    desc = Column(String)   # 商品描述
    price = Column(Float)   # 商品实际价格
    market_price = Column(Float)  # 商品原价/市场价
    stock = Column(Integer)  # 库存
    views = Column(Integer)  # 浏览量
    sales = Column(Integer)  # 销量
    online = Column(SmallInteger)  # 商品上架
    sort = Column(Integer)   # 排序字段


class GoodsImage(Base):
    # 商品图片

    __tablename__ = 'ft_goods_img'

    id = Column(Integer, primary_key=True, autoincrement=True)
    goods_id = Column(Integer)
    pic = Column(String)   # 商品图片
    desc = Column(String)  # 描述


class Banner(Base):
    # Banner

    __tablename__ = 'ft_banner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    goods_id = Column(Integer)
    pic = Column(String)
    sort = Column(Integer)
