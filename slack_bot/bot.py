# -*- coding: utf-8 -*-
from datetime import datetime, timezone
import os

from kudos.user_kudos_repository import UserKudosRepository
from slack_bot import message
from slackclient import SlackClient

# To remember which teams have authorized your app and what tokens are
# associated with each team, we can store this information in memory on
# as a global object.
# FIXME When your bot is out of development, it's best to save to a more persistent memory store.
authed_teams = {}


class Bot(object):
    """ Instantiates a Bot object to handle Slack onboarding interactions."""

    def __init__(self, logger, postgres_connection):
        super(Bot, self).__init__()

        # TODO there has to be a better way of getting a logger than passing it from Flask
        self.logger = logger

        # bot identitiy
        self.name = "gonzo"
        self.emoji = ":peanut_butter_jelly_time:"

        # Security & verification
        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")

        self.user_kudos_repo = UserKudosRepository(postgres_connection)

        # NOTE: Python-slack requires a client connection to generate
        # an oauth token. We can connect to the client without authenticating
        # by passing an empty string as a token and then reinstantiating the
        # client with a valid OAuth token once we have one.
        # FIXME this BOT_TOKEN is not the right way to do OAuth
        self.bot_token = os.environ.get("BOT_TOKEN")
        self.client = SlackClient(self.bot_token)

        self.messages = {}

    def auth(self, code):
        auth_response = self.client.api_call(
            "oauth.access",
            client_id=self.oauth["client_id"],
            client_secret=self.oauth["client_secret"],
            code=code
        )
        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                     auth_response["bot"]["bot_access_token"]}
        self.client = SlackClient(authed_teams[team_id]["bot_token"])

    def onboarding_message(self, team_id, user_id):
        if self.messages.get(team_id):
            self.messages[team_id].update({user_id: message.Message()})
        else:
            self.messages[team_id] = {user_id: message.Message()}
        message_obj = self.messages[team_id][user_id]
        message_obj.channel = self.open_dm(user_id)
        message_obj.create_attachments()
        post_message = self.client.api_call("chat.postMessage",
                                            channel=message_obj.channel,
                                            username=self.name,
                                            icon_emoji=self.emoji,
                                            text=message_obj.text,
                                            attachments=message_obj.attachments
                                            )
        timestamp = post_message["ts"]
        message_obj.timestamp = timestamp

    def give_kudos(self, user, event_ts, channel, text, client_msg_id):
        print(f"attempting to give someone kudos from {self}")

        self.user_kudos_repo.create(user, event_ts, channel, text, client_msg_id)
        kudos_count = self.user_kudos_repo.get_count(user)

        post_message = self.client.api_call("chat.postMessage",
                                            channel=channel,
                                            text=f"Whoop whoop. {user} now has {kudos_count} kudos!"
                                            )
        print(post_message)
