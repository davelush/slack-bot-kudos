from unittest import TestCase
from org.davelush.kudos.sentiment import Sentiment

class TestSentiment(TestCase):
    sentiment = Sentiment()

    def test_positive_sentiment(self):
        result = self.sentiment.is_positive_emoji(":stars:")
        self.assertTrue(result)

    def test_negative_sentiment(self):
        result = self.sentiment.is_positive_emoji(":shit:")
        self.assertFalse(result)

    def test_none_sentiment(self):
        result = self.sentiment.is_positive_emoji(None)
        self.assertFalse(result)

    def test_spot_emoji(self):
        text = "here is a string with an :emoji: in the middle"
        result = self.sentiment.contains_emoji(text)
        print(result)
        self.assertEqual([":emoji:"], result, "match is not a list with a single emoji")

    def test_spot_user(self):
        text = "here is a string with a <@username> in the middle"
        result = self.sentiment.contains_user(text)
        print(result)
        self.assertEqual(["<@username>"], result, "match is not a list with a single username")
