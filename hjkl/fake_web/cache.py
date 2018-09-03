# coding: utf-8


def can_cache(conn, request):
    return True


def hash_request(request):
    # generate a hash string for each request
    return ''


def cache_request(conn, request, callback):
    if not can_cache(conn, request):
        return callback(request)

    page_key = 'cache:' + hash_request(request)
    content = conn.get(page_key)

    if not content:
        content = callback(request)
        conn.setex(page_key, content, 300)

    return content


