from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.slack_install_handler import SlackInstallHandler


class TestSlackInstallHandler(TestCase):

    def test_get_happy(self):
        with patch("org.davelush.slack_bot.bot.Bot") as mock_slack_bot:
            with patch("org.davelush.slack_bot.slack_install_handler.render_template") as mock_render:
                mock_slack_bot.oauth = {"client_id": "id", "scope": "scope"}
                slack_install_handler = SlackInstallHandler(**{"py_bot": mock_slack_bot})
                result = slack_install_handler.get()
                
                self.assertIsNotNone(result)
