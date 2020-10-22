from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.slack_event_handler import hears
from org.davelush.slack_bot.tests.sample_events import app_mention_event, verification_token


class TestSlackEventHandler(TestCase):

    def test_hears_incorrect_verification(self):
        pass
        # with patch("org.davelush.slack_bot.slack_event_handler.request") as mock_request:
        #     with patch("org.davelush.slack_bot.slack_event_handler.make_response") as mock_make_response:
        #         with patch("org.davelush.slack_bot.bot.Bot") as mock_bot:
        #
        #             mock_bot.verification = "invalid-verification"
        #             mock_request.data = app_mention_event
        #
        #             mock_make_response.assert_any_call(403)
        #
        #             response = hears(mock_bot)
