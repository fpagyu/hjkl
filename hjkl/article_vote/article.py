# coding: utf-8
import redis
import time

pool = redis.ConnectionPool(**{
    'max_connections': 150,
    'host': 'localhost',
    'port': 6379,
    'password': 'password'
})


def redis_cli():
    return redis.Redis(connection_pool=pool)


class Article:

    ONE_WEEK_IN_SECONDS = 7 * 86400
    # 每票获取的分数
    VOTE_SCORE = 432

    # 每页显示的文章数量
    ARTICLE_PER_PAGE = 25

    @classmethod
    def article_vote(cls, conn, user, article):
        """ 文章投票
        :param conn:
        :param user:
        :param article:
        :return:
        """
        # 计算文章投票截止时间
        cutoff = int(time.time()) - cls.ONE_WEEK_IN_SECONDS
        if conn.zscore('time:', article) < cutoff:
            return

        article_id = article.partition(':')[-1]
        if conn.sadd('voted: ' + article_id, user):
            conn.zincrby('score:', article, cls.VOTE_SCORE)
            conn.hincrby(article, 'votes', 1)

    @classmethod
    def post_article(cls, conn, user, title, link):
        """ 发布并获取文章
        :return:
        """
        article_id = conn.incr('article:')

        voted = 'voted:{}'.format(article_id)
        conn.sadd(voted, user)
        conn.expire(voted, cls.ONE_WEEK_IN_SECONDS)

        now = int(time.time())
        article = 'article:{}'.format(article_id)
        conn.hmset(article, {
            'title': title,
            'link': link,
            'poster': user,
            'time': now,
            'votes': 1,
        })
        conn.zadd('score:', article, now+cls.VOTE_SCORE)
        conn.zadd('time:', article, now)
        return article_id

    @classmethod
    def get_articles(cls, conn, page, order='score:'):
        start = (page - 1) * cls.ARTICLE_PER_PAGE
        end = start + cls.ARTICLE_PER_PAGE - 1

        ids = conn.zrevrange(order, start, end)
        articles = []
        for id in ids:
            article_data = conn.hgetall(id)
            article_data['id'] = id
            articles.append(article_data)

        return articles

    @classmethod
    def add_remove_groups(cls, conn, article_id, to_add=(), to_remove=()):
        article = 'article:{}'.format(article_id)
        for group in to_add:
            conn.sadd('group:' + group, article)
        for group in to_remove:
            conn.srem('group:' + group, article)

    @classmethod
    def get_group_articles(cls, conn, group, page, order='score:'):
        key = order + group
        if not conn.exists(key):
            conn.zinterstore(key,
                             ['group: ' + group, order],
                             aggregate='max',
                             )
            conn.expire(key, 60)
        return cls.get_articles(conn, page, key)
