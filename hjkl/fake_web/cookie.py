# coding:utf-8
import time


class CookieService:
    """ 实现一个cookie令牌环服务
    """
    QUIT = False
    # Redis 只会保留最新的1000万个会话
    LIMIT = 10000000

    @classmethod
    def check_token(cls, conn, token):
        return conn.hget('login:', token)

    @classmethod
    def update_token(cls, conn, token, user, item=None):
        timestamp = int(time.time())
        conn.hset('login:', token, user)
        conn.zadd('recent:', token, timestamp)
        if item:
            # 记录用户浏览过的商品
            conn.zadd('viewed:' + token, item, timestamp)
            # 移除旧的记录, 只保留用户最近浏览过的25个商品
            conn.zremrangebyrank('viewed:' + token, 0, -26)

    # @classmethod
    # def clean_sessions(cls, conn):
    #     while not cls.QUIT:
    #         # 找到目前已有的令牌环数量
    #         size = conn.zcard('recent:')
    #         if size <= cls.LIMIT:
    #             time.sleep(1)
    #             continue
    #
    #         end_index = min(size - cls.LIMIT, 100)
    #         tokens = conn.zrange('recent:', 0, end_index-1)
    #
    #         session_keys = []
    #         for token in tokens:
    #             session_keys.append('viewed:' + token)
    #
    #         conn.delete(*session_keys)
    #         conn.hdel('login:', *tokens)
    #         conn.zrem('recent:', *tokens)
    @classmethod
    def clean_full_session(cls, conn):
        while not cls.QUIT:
            size = conn.zcard('recent:')
            if size <= cls.LIMIT:
                time.sleep(1)
                continue

            end_index = min(size - cls.LIMIT, 100)
            sessions = conn.zrange('recent:', 0, end_index-1)

            session_keys = []
            for sess in sessions:
                session_keys.append('viewed:' + sess)
                session_keys.append('cart:' + sess)

            conn.delete(*session_keys)
            conn.hdel('login:', *sessions)
            conn.zrem('recent:', *sessions)


