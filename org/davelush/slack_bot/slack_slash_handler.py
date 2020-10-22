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

        elif slash_text.strip() == "givers this month":
            the_date = datetime.datetime.now()
            response = self.py_bot.get_giver_stats(the_date.year, the_date.month)

        elif slash_text.strip() == "givers last month":
            the_date = datetime.datetime.now() - datedelta.MONTH
            response = self.py_bot.get_giver_stats(the_date.year, the_date.month)

        elif slash_text.strip() == "messages this month":
            the_date = datetime.datetime.now()
            response = self.py_bot.get_messages(the_date.year, the_date.month)

        elif slash_text.strip() == "messages last month":
            the_date = datetime.datetime.now() - datedelta.MONTH
            response = self.py_bot.get_messages(the_date.year, the_date.month)

        elif slash_text.strip() == "this month":
            the_date = datetime.datetime.now()
            response = self.py_bot.get_recipient_stats(the_date.year, the_date.month)

        elif slash_text.strip() == "last month":
            the_date = datetime.datetime.now() - datedelta.MONTH
            response = self.py_bot.get_recipient_stats(the_date.year, the_date.month)

        elif slash_text.startswith("tell "):
            response = "this will be anonymous kudos gifting"

        elif slash_text.strip() == "help":
            response = "*Try the following useful commands*\n" \
                        " • Give someone kudos by mentioning their name and giving them a :star: :star2: :stars: :cookie: :chocfish: :chocfish2:\n" \
                        " • `/kudos` - Kudos givers and receivers for all time\n" \
                        " • `/kudos last month` - Recipient stats for last month\n" \
                        " • `/kudos this month` - Recipient stats for this month\n" \
                        " • `/kudos givers last month` - Giver stats for last month\n" \
                        " • `/kudos givers this month` - Giver stats for this month\n" \
                        " • `/kudos messages last month` - Messages for last month\n" \
                        " • `/kudos messages this month` - Messages for this month"
        return {"text": response}

        # " • `/kudos tell @user your message here` - Anonymous kudos for a user\n"\
