from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.bot import Bot


class TestBot(TestCase):

    def test_give_kudos(self):
        with patch("slackclient.SlackClient") as mock_slack_client:
            with patch("psycopg2.connect") as mock_conn:
                bot = Bot(mock_conn, "", "", "")
                mock_conn.cursor.return_value.fetchone.return_value = [0]
                mock_slack_client.api_call.return_value = "OK"
                result = bot.give_kudos("user", 1, "channel", "text", "message_id", "event_id")
                assert result == True

    def test_already_has_kudos(self):
        with patch("slackclient.SlackClient") as mock_slack_client:
            with patch("psycopg2.connect") as mock_conn:
                bot = Bot(mock_conn, "", "", "")
                mock_conn.cursor.return_value.fetchone.return_value = [1]
                mock_slack_client.api_call.return_value = "OK"
                result = bot.give_kudos("user", 1, "channel", "text", "message_id", "event_id")
                assert result == False

