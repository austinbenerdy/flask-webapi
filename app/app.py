import sys

from controller.userController import UserController
from util.decorators.tokenRequired import token_required
from core.container import Container
from flask import Flask
from dependency_injector.wiring import inject, Provide, Provider

app = Flask(__name__)
container = Container()
container.wire(modules=[sys.modules[__name__]])
app.container = container


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'Hey there'

"""
The code snippet below is supposed to work. However what was
happening is that the Provide[Container.user_controller] was 
returning an instance of the Provide and not an instance of
the UserController. I couldn't figure out why that is that case
so I tried calling the user_controller property of the container
instance directly and that seemed to work fine. 
-------------- Begin Code ------------------------
@app.route('/user', methods=['GET'])
@inject
@token_required
def user(user_controller: UserController = Provide[Container.user_controller]):
    return user_controller().read()
------------- End Code ---------------------------
"""

@app.route('/test', methods=['GET'])
@inject
@token_required
def test():
    user_controller = container.user_controller()
    return user_controller.read()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
