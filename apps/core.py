# coding: utf-8
from .settings import ENGINES


def engine(name=''):
    if name:
        return ENGINES[name]

    return ENGINES['default']
