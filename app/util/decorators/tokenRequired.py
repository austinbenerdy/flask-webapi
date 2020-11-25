
from functools import wraps
import logging
import flask

def token_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        apikey = flask.request.headers.get('x-api-key')
        print(apikey)
        if (apikey):
            flask.app.current_user = "USERNAME"
        else:
            flask.app.current_user = None
        return func(*args, **kwargs)

    return decorated_function
