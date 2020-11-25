
from controller.abstract.apiRestController import APIRestController

import flask


class UserController(APIRestController):

    def __init__(self):
        self.apiType = 'restful'

    def read(self):
        value = super(UserController, self).read();
        if (flask.app.current_user):
            return "Hello " + flask.app.current_user
        else:
            return value