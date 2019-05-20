# -*- coding: utf-8 -*-
import logging
import os

from org.davelush.kudos.sayings import Sayings
from org.davelush.kudos.user_kudos_repository import UserKudosRepository
from slackclient import SlackClient

# FIXME When your bot is out of development, it's best to save to a more persistent memory store.
authed_teams = {}


class Bot(object):
    """ Instantiates a Bot object to handle Slack onboarding interactions."""

    def __init__(self, postgres_connection, client, client_id, client_secret):
        super(Bot, self).__init__()
        self.oauth = {"client_id": client_id,
                      "client_secret": client_secret,
                      "scope": "bot"}
        self.user_kudos_repo = UserKudosRepository(postgres_connection)
        self.verification = os.environ.get("VERIFICATION_TOKEN") #TODO this is being used in the event_handler. Is it necessary?
        self.client = client
        self.messages = {}

    #TODO Need to understand the lifetime of the bot_token that comes back from this oauth.access call. When
    # I currently use a bot_token it is hard-coded via an environment variable. This method looks to persist
    # a bot_token per authenticated team, facilitating a single service enabling bot installs for multiple
    # Slack teams. Task is to understand and prove / disprove this and clean up approach
    def auth(self, code):
        auth_response = self.client.api_call(
            "oauth.access",
            client_id=self.oauth["client_id"],
            client_secret=self.oauth["client_secret"],
            code=code
        )
        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token": auth_response["bot"]["bot_access_token"]}
        self.client = SlackClient(authed_teams[team_id]["bot_token"])

    def give_kudos(self, user, event_ts, channel, text, client_msg_id, event_id):
        logging.info(f"attempting to give someone kudos from {self} with event_id = {event_id}")
        if not self.user_kudos_repo.event_exists(event_id):
            self.user_kudos_repo.create(user, event_ts, channel, text, client_msg_id, event_id)
            kudos_count = self.user_kudos_repo.get_count(user)

            post_message = self.client.api_call("chat.postMessage",
                                                channel=channel,
                                                text=Sayings.received_kudos_saying(user, kudos_count)
                                                )
            logging.info(post_message)
            return True
        return False

    def get_leaderboard(self):
        user_kudos = self.user_kudos_repo.get_kudos_amounts()
        text = ":rocket: *Kudos Leaderboard* :rocket:\n"
        i = 1
        for user in user_kudos:
            text += f"{i}. {user.get('user_id')} has {user.get('kudos_count')} kudos\n"
            i = i+1
        return text

    def get_stats(self, year, month):
        user_kudos = self.user_kudos_repo.get_kudos_amounts_for_month(year, month)
        text = f"No one gave each other any kudos in {year}/{month}"
        if len(user_kudos) > 0:
            text = f":rocket: *Kudos Recipients for {year}/{month}* :rocket:\n"
            i = 1
            for user in user_kudos:
                text += f"{i}. {user.get('user_id')} has {user.get('kudos_count')} kudos\n"
                i = i+1
        return text

