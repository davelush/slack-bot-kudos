import logging

from flask_restful import Resource
from flask import request

class SlackSlashHandler(Resource):
    def __init__(self, **kwargs):
        pass

    def post(self):
        logging.info(request)
        logging.info(request.form)
        return "ohh... hello"
