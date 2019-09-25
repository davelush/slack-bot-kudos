import json
import logging

from flask import request, make_response
from flask_restful import Resource

from org.davelush.kudos.sentiment import Sentiment


def event_handler(event_type, slack_event, py_bot):
    # team_id = slack_event["team_id"]
    logging.debug(f"{event_type} and body [{slack_event}]")

    if event_type == "message":
        # initialise some field based on the message content
        text = slack_event.get("event").get("text")
        channel_id = slack_event.get("event").get("channel")
        event_ts = slack_event.get("event").get("ts")
        event_id = slack_event.get("event_id")
        client_msg_id = slack_event.get("event").get("client_msg_id")
        sending_user = f"<@{slack_event.get('event').get('user')}>"

        # get the emojis and users out of the message text
        sentiment = Sentiment()
        message_emojis = sentiment.get_positive_emojis(text)
        message_users = sentiment.get_users(text)

        # give kudos to individuals
        if message_emojis[0] == True and message_users[0] == True:
            if sending_user in message_users[1]:
                py_bot.block_self_kudos(sending_user, event_ts, channel_id, text, client_msg_id, event_id)
            else:
                for user in message_users[1]:
                    print(f"attempting to give kudos to user based on : {text}")
                    print(f"{event_type} : {slack_event}")
                    py_bot.give_kudos(user, sending_user, event_ts, channel_id, text, client_msg_id, event_id)

        # synchronous acknowledgement response
        message = "Updated kudos and sent response message"
        return make_response(message, 200, )

    elif event_type == "reaction_removed":
        return make_response("Not yet implemented", 200, )
    elif event_type == "emoji_changed":
        return make_response("Not yet implemented", 200, )

    message = "You have not added an event handler for the %s" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


def hears(py_bot):
    slack_event = json.loads(request.data)

    logging.info(slack_event)

    # Echo Slack's challenge when you subscribe to events
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    # Verify it's actually Slack sending us events
    if py_bot.verification != slack_event.get("token"):
        message = f"Invalid Slack verification token: {slack_event['token']} pyBot has: {py_bot.verification}"
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    # Handle any events correctly
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event, py_bot)

    # Canned response for events we're not subscribed to
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids you're looking for.", 404,
                         {"X-Slack-No-Retry": 1})

class SlackEventHandler(Resource):

    def __init__(self, **kwargs):
        self.py_bot = kwargs.get('py_bot')

    def post(self):
        return hears(self.py_bot)

    def get(self):
        return hears(self.py_bot)





