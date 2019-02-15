from flask import Flask, jsonify, request

from flask_restful import Api
from sign_in_service.validate_user_credentials import ValidateUser
from hello_service.say_hello import SayHello
from hello_world.index import HelloWorld


def create_flask_app(name):
    app = Flask(name)
    return app


if __name__ == "__main__":
    app = create_flask_app(__name__)
    api = Api(app)
    api.add_resource(HelloWorld, '/')
    api.add_resource(
        ValidateUser, '/sign_in_service/')
    api.add_resource(
        SayHello, '/say_hello/<name>')
    app.run(host='0.0.0.0', debug=True)
