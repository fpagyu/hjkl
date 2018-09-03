# coding: utf-8
import redis

__all__ = ['redis_client']

RedisConfig = {
    'max_connections': 150,
    'host': '127.0.0.1',
    'port': '6379',
    'password': 'lovewith99',
}


pool = redis.ConnectionPool(**RedisConfig)


def redis_client():
    return redis.Redis(connection_pool=pool)
