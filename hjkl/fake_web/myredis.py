# coding: utf-8
import redis

pool = redis.ConnectionPool(**{
    'max_connections': 150,
    'host': 'localhost',
    'port': '6379',
    'password': 'lovewith99',
})


def redis_client():
    return redis.Redis(connection_pool=pool)
