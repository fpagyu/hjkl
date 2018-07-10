# coding: utf-8
<<<<<<< Updated upstream


PROJECT_NAME = 'hjkl'

DATABASES = {
    'default': 'mysql+pool://yuzj:880629@localhost:3306/hjkl?charset=utf8&max_connections=60&stale_timeout=180',
    # 'default': 'mysql://root:880629@localhost:3306/hjkl?charset=utf8',
}

DEV_DATABASES = {
    'default': 'mysql+pool://yuzj:880629@localhost:3306/hjkl?charset=utf8&max_connections=60&stale_timeout=180',
    # 'theme_img': 'mysql://username:password@host:port/database',
    'theme_img': {
        'scheme': 'mysql',
        'database': '******',
        'host': '*************************',
        'port': 3306,
        'user': 'invitdb',
        'password': '***********'
    },
=======
import os
from sqlalchemy import create_engine

PROJECT_NAME = 'hjkl'

DEBUG = os.environ.get('FLASK_ENV', '') == "development"

ENGINES = {
    "default": create_engine('mysql+pymysql://yuzj:880629@127.0.0.1:3306/hjkl?encoding=utf8', encoding='utf-8',
                             pool_size=10, pool_recycle=900, pool_timeout=3, max_overflow=5, echo=DEBUG)
>>>>>>> Stashed changes
}
