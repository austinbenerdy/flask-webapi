from controller.userController import UserController
from util.decorators.tokenRequired import token_required
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/hello')
def hello():
    return 'Hey there'


@app.route('/user', methods=['GET'])
@token_required
def user():
    user_controller = UserController()
    return user_controller.read()


if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')