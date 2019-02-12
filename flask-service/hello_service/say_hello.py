from flask import jsonify, request
import logging

from flask_restful import Resource, reqparse

logger = logging.getLogger(__name__)


class SayHello(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        logger.info("0; Say Hello service created")

    def get(self, name=None):
        logger.info("0; received hello request from '{}'".format(name))
        return "Hello '{}', Welcome to Python flask in Docker!".format(name)
