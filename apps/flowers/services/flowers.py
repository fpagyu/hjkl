# coding: utf-8
from sqlalchemy.orm import sessionmaker

from apps.flowers.app_config import engine
from apps.flowers.models import Flower


class FlowerService(object):

    @classmethod
    def retrieve(cls):
        pass

    @classmethod
    def get_by_pk(cls, pk):
        session = sessionmaker(bind=engine, autocommit=True)()

        return session.query(Flower).filter_by(id=pk).first()
