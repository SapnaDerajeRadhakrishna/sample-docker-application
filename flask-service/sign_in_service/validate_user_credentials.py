from flask import jsonify, request
import logging

from flask_restful import Resource, reqparse

logger = logging.getLogger(__name__)


class ValidateUser(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        logger.info("0; ValidateUser service created")

    def get(self):
        response = jsonify({'result': "ok"})
        return response
