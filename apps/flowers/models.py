# coding: utf-8
from sqlalchemy import MetaData, Table, Column, Integer, String, Text
from sqlalchemy.orm import mapper

# from apps import engine
from .app_config import engine

meta = MetaData(bind=engine)


rd_flower = Table('rd_flower', meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(32), server_default=''),
                  Column('path', String(200), server_default=''),
                  Column('content', Text))


class Flower(object):

    def __init__(self, id, name, path, content):
        self.id = id
        self.name = name
        self.path = path
        self.content = content


mapper(Flower, rd_flower)

# meta.create_all()
