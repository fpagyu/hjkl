# coding: utf-8
import flask
<<<<<<< Updated upstream
import importlib

from playhouse.flask_utils import FlaskDB

from .db import db_proxy
from .service import BaseService

__all__ = ['App', 'Settings', 'BaseService', 'db_proxy']


Settings = importlib.import_module('apps.settings')


class App:

    @classmethod
    def get_app(cls, name: str=''):
        app = getattr(cls, '_app', None)
        if app is not None:
            return app

        if not name:
            name = Settings.PROJECT_NAME

        app = flask.Flask(name)
        app.config.from_object(Settings)
        FlaskDB(app, db_proxy.obj)

        setattr(cls, '_app', app)

        return app
=======

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
>>>>>>> Stashed changes
