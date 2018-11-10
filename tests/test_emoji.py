
from kudos.emoji import Emoji

class TestEmoji(object):
    emoji = Emoji()

    def test_positive_emoji(self):
        result = self.emoji.is_positive("stars")
        assert result is True

    def test_negative_emoji(self):
        result = self.emoji.is_positive("shit")
        assert result is False

    def test_none_emoji(self):
        result = self.emoji.is_positive(None)
        assert result is False
