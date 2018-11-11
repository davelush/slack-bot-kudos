
from kudos.sentiment import Sentiment

class TestSentiment(object):
    sentiment = Sentiment()

    def test_positive_sentiment(self):
        result = self.sentiment.is_positive(":stars:")
        assert result is True

    def test_negative_sentiment(self):
        result = self.sentiment.is_positive(":shit:")
        assert result is False

    def test_none_sentiment(self):
        result = self.sentiment.is_positive(None)
        assert result is False
