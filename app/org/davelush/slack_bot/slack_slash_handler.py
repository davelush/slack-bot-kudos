import json
import logging

from flask_restful import Resource
from flask import request

class SlackSlashHandler(Resource):
    def __init__(self, **kwargs):
        self.py_bot = kwargs.get('py_bot')

    def post(self):
        logging.info(request)
        logging.info(request.form)
        slash_text = request.form.get("text")
        if len(slash_text.strip()) == 0:
            response = self.py_bot.get_leaderboard()
            logging.info(json.dumps(response))
            return response
        elif slash_text.startswith("tell "):
            return "this will be anonymous kudos gifting"
        else:
            return "Sorry... I'm not quite sure what you mean?"
