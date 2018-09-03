# coding: utf-8

# 使用redis实现购物车


class CartService:

    @classmethod
    def add_to_card(cls, conn, session, item, count):
        if count <= 0:
            conn.hrem('cart:' + session, item)
        else:
            conn.hset('cart:' + session, item, count)
