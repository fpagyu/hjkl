# coding: utf-8
from apps import app

# module = __import__('apis.flowers')
# print(module.app is app)
# print(id(module.flowers.app))
# print(id(app))

__import__('apis.flowers')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
