"""
Само веб приложение.

"""
from flask import request

from views import *
from settings import app


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['FLASK_DEBUG'])
