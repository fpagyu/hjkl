# coding: utf-8
import flask

from .settings import PROJECT_NAME
from .core import engine

__all__ = ['app', 'engine']

app = flask.Flask(PROJECT_NAME)


# def get_app():
#     global app
#     if app is None:
#         app = flask.Flask(PROJECT_NAME)
#
#     return app
#
#     loop = asyncio.get_event_loop()
