import datetime
import json
import logging

import datedelta
from flask_restful import Resource
from flask import request


class SlackSlashHandler(Resource):
    def __init__(self, **kwargs):
        self.py_bot = kwargs.get('py_bot')

    def post(self):
        slash_text = request.form.get("text")
        response = "I'm not sure what you mean. Try `/kudos help` for commands"
        if len(slash_text.strip()) == 0:
            response = self.py_bot.get_leaderboard()
            logging.info(json.dumps(response))
        elif slash_text.strip() == "this month":
            the_date = datetime.datetime.now()
            response = self.py_bot.get_stats(the_date.year, the_date.month)
        elif slash_text.strip() == "last month":
            the_date = datetime.datetime.now() - datedelta.MONTH
            response = self.py_bot.get_stats(the_date.year, the_date.month)
        elif slash_text.startswith("tell "):
            response = "this will be anonymous kudos gifting"
        elif slash_text.strip() == "help":
            response = "*Try the following useful commands*\n"\
                        " • `/kudos tell @user your message here` - Anonymous kudos for a user\n"\
                        " • `/kudos` - Kudos givers and receivers for all time\n" \
                        " • `/kudos last month` - Stats for last month\n" \
                        " • `/kudos this month` - Stats for this month\n"
        return {"text": response}
