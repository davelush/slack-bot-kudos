import pytest

from slack_bot.message import Message

class TestMessage(object):

    def test_one(self):
        message = Message()
        assert True
