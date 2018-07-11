# coding: utf-8
import os
from sqlalchemy import create_engine

PROJECT_NAME = 'hjkl'

DEBUG = os.environ.get('FLASK_ENV', '') == "development"

ENGINES = {
    "default": create_engine('mysql+pymysql://yuzj:880629@127.0.0.1:3306/hjkl?charset=utf8',
                             pool_size=30, pool_recycle=900, pool_timeout=5, max_overflow=5, echo=DEBUG)
}
