from unittest import TestCase

from org.davelush.slack_bot.message import Message


class TestMessage(TestCase):

    def test_one(self):
        message = Message()
        assert True
