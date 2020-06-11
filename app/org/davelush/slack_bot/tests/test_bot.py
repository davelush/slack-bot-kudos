from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.bot import Bot

overall_query_result = [["some_id_1", 3], ["some_id_2", 2]]
monthly_query_result = [["some_id_3", 5], ["some_id_4", 1]]

class TestBot(TestCase):

    def test_give_kudos(self):
        with patch("slackclient.client.SlackClient") as mock_slack_client:
            with patch("psycopg2.connect") as mock_conn:
                bot = Bot(mock_conn, mock_slack_client, "", "")
                mock_conn.cursor.return_value.fetchone.return_value = [0]
                mock_slack_client.api_call.return_value = "OK"
                result = bot.give_kudos("user", "giver", 1, "channel", "text", "message_id", "event_id")
                self.assertTrue(result)

    def test_already_has_kudos(self):
        with patch("slackclient.client.SlackClient") as mock_slack_client:
            with patch("psycopg2.connect") as mock_conn:
                bot = Bot(mock_conn, mock_slack_client, "", "")
                mock_conn.cursor.return_value.fetchone.return_value = [1]
                mock_slack_client.api_call.return_value = "OK"
                result = bot.give_kudos("user", "giver", 1, "channel", "text", "message_id", "event_id")
                self.assertFalse(result)

    def test_get_leaderboard(self):
        with patch("slackclient.client.SlackClient") as mock_slack_client:
            with patch("psycopg2.connect") as mock_conn:
                bot = Bot(mock_conn, mock_slack_client, "", "")
                mock_conn.cursor.return_value.__iter__.return_value = overall_query_result
                result = bot.get_leaderboard()
                self.assertEqual(result, ':rocket: *Kudos Leaderboard* :rocket:\n1. some_id_1 has 3 kudos\n2. some_id_2 has 2 kudos\n')


    def test_get_stats(self):
        with patch("slackclient.client.SlackClient") as mock_slack_client:
            with patch("psycopg2.connect") as mock_conn:
                bot = Bot(mock_conn, mock_slack_client, "", "")
                mock_conn.cursor.return_value.__iter__.return_value = monthly_query_result
                result = bot.get_recipient_stats(2019, 5)
                self.assertEqual(result, ':rocket: :rocket: *Biggest Kudos Receivers for 2019/5* :rocket: :rocket:\n1. some_id_3 has received 5 kudos\n2. some_id_4 has received 1 kudos\n')
