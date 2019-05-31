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
        text = "here is a string with an :star: in the middle"
        result_bool, result_list = self.sentiment.get_positive_emojis(text)
        print(f"{result_bool} : {result_list}")
        self.assertTrue(result_bool)
        self.assertEqual([":star:"], result_list, "match is not a list with a single emoji")

    def test_spot_user(self):
        text = "here is a string with a <@usernamea> in the middle"
        result_bool, result_list = self.sentiment.get_users(text)
        print(f"{result_bool} : {result_list}")
        self.assertTrue(result_bool)
        self.assertEqual(["<@usernamea>"], result_list, "match is not a list with a single username")

    def test_spot_two_users(self):
        text = "here is a string with a <@usernamea> and a second <@usernameb> in"
        result_bool, result_list = self.sentiment.get_users(text)
        self.assertTrue(result_bool)
        self.assertEqual(["<@usernamea>", "<@usernameb>"], result_list, "match is not two usernames in order")
