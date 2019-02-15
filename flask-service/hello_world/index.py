from flask import jsonify, request
import logging

from flask_restful import Resource, reqparse

logger = logging.getLogger(__name__)


class HelloWorld(Resource):

    def __init__(self):
        logger.info("0;HelloWorld service created")

    def get(self):
        return "Hello World"
