from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.bot import Bot


class TestBot(TestCase):

    def happy_test(self):
        with patch("slackclient.SlackClient") as mock_slack_client:
            with patch("org.davelush.kudos.user_kudos.repository.UserKudosRepository") as mock_kudos_repo:
                bot = Bot(None, None, None, None)
                mock_kudos_repo.event_exists.return_value = False
                mock_kudos_repo.create.return_value = 5
                mock_slack_client.api_call.return_value = "OK"
                bot.give_kudos("user", 1, "channel", "text", "message_id", "event_id")


