from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.slack_post_install_handler import SlackPostInstallHandler


class TestSlackPostInstallHandler(TestCase):

    def test_happy_get(self):
        with patch("org.davelush.slack_bot.bot.Bot") as mock_slack_bot:
            with patch("org.davelush.slack_bot.slack_post_install_handler.render_template") as mock_render:
                with patch("org.davelush.slack_bot.slack_post_install_handler.request") as mock_request:
                    slack_post_install_handler = SlackPostInstallHandler(**{"py_bot": mock_slack_bot})
                    result = slack_post_install_handler.get()
                    self.assertIsNotNone(result)

    def test_happy_post(self):
        with patch("org.davelush.slack_bot.bot.Bot") as mock_slack_bot:
            with patch("org.davelush.slack_bot.slack_post_install_handler.render_template") as mock_render:
                with patch("org.davelush.slack_bot.slack_post_install_handler.request") as mock_request:
                    slack_post_install_handler = SlackPostInstallHandler(**{"py_bot": mock_slack_bot})
                    result = slack_post_install_handler.post()
                    self.assertIsNotNone(result)