
from controller.abstract.apiRestController import APIRestController
from service.userService import UserService

import flask


class UserController(APIRestController):

    def __init__(self, user_service: UserService):
    # def __init__(self):
        self.apiType = 'restful'
        self.userService = user_service

    def read(self):

        value = super(UserController, self).read()
        newValue = self.userService.read()
        if (flask.app.current_user):
            return "Hello " + flask.app.current_user
        elif (newValue):
            return "Service Worked"
        else:
            return value