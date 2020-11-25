from controller.userController import UserController
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hello')
def hello():
    return 'Hey there'

@app.route('/user', methods=['GET'])
def user():
    userController = UserController()
    return userController.read()


if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')