"""
Настройки приложения.

"""
import os
import logging
from logging.handlers import RotatingFileHandler
from urllib.parse import quote_plus

from flask import Flask
from flask_pymongo import PyMongo

from environments import EnvironmentFileToDict, EnvironmentOsToDict


#########################
# Переменные окружения. #
#########################
ENV_DICT = {}
ENV_FILE_FROM_FILE = EnvironmentFileToDict()
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

if os.path.exists(ENV_FILE):
    ENV_FILE_FROM_FILE.load(ENV_FILE)
    ENV_DICT.update(ENV_FILE_FROM_FILE)

ENV_DICT_FROM_OS = EnvironmentOsToDict()
ENV_DICT_FROM_OS.load()

ENV_DICT.update(ENV_DICT_FROM_OS)

ENVIRONMENT = ENV_DICT.get('ENVIRONMENT', 'production')


#########################
# Инициализация.        #
#########################
app = Flask(__name__, static_url_path=ENV_DICT.get('static_url', '/static'))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#########################
# Настройка логера.     #
#########################
LOG_FOLDER = ENV_DICT.get('LOG_FOLDER', BASE_DIR)
handler = RotatingFileHandler(
    os.path.join(LOG_FOLDER, ENV_DICT.get('LOG_FILE_NAME', 'nlp-service.log')),
    maxBytes=1024 * 1024 * 1024 * 100,
    backupCount=20,
    encoding='utf-8'
)
handler.setLevel(logging.DEBUG)
app.logger.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(levelname)s %(asctime)s %(process)d %(module)s %(message)s'))
app.logger.addHandler(handler)


#########################
# Настройка приложения. #
#########################
app.config['HOST'] = ENV_DICT.get('BASE_DOMAIN', '0.0.0.0')
app.config['PORT'] = ENV_DICT.get('SERVER_PORT', 5000)
app.config['FLASK_DEBUG'] = ENV_DICT.get('FLASK_DEBUG', False)
app.config['FLASK_ENV'] = ENVIRONMENT
app.config['MONGO_URI'] = 'mongodb://{}:{}@{}:{}/{}'.format(
    quote_plus(ENV_DICT.get('MONGO_USER', '')), quote_plus(ENV_DICT.get('MONGO_PASSWORD', '')),
    ENV_DICT.get('MONGO_HOST', '0.0.0.0'), ENV_DICT.get('MONGO_PORT', 27017),
    ENV_DICT.get('MONGO_DATABASE', '')
)
app.config['mongo'] = PyMongo(app)
