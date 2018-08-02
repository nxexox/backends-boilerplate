"""
Вью для проекта.

"""
from flask import request, abort, make_response, jsonify
from flask.views import MethodView

from settings import app


@app.errorhandler(404)
def not_found(error):
    """
    404 ошибка.

    """
    return make_response(jsonify(
        {'error': 'Not found', 'messages': getattr(error, 'description', None)}
    ), 404)


@app.errorhandler(400)
def bad_request(error):
    """
    400 ошибка.

    """
    return make_response(jsonify(
        {'error': 'Bad request', 'messages': getattr(error, 'description', None)}
    ), 400)


@app.errorhandler(500)
def not_found(error):
    """
    500 ошибка.

    """
    return make_response(jsonify(
        {'error': 'Uups, sorry =)', 'messages': getattr(error, 'description', None)}
    ), 500)


# your code ...
