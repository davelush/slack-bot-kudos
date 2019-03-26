# -*- coding: utf-8 -*-
"""
Module for encapsulating the Sentiment class
"""
import re


#TODO it'd be good it this stored all emojis within a message and provided a score of positive / negative across all of
# them
#TODO the set of emojis should be configurable


class Sentiment(object):
    """
    Sentiment class finds emojis in a message and checks allows checking of whether an emoji is positive or not
    """

    positive_emojis = [":star:",
                       ":star2:",
                       ":stars:",
                       ":cookie:"]

    def __init__(self):
        pass

    def is_positive_emoji(self, emoji):
        if emoji in self.positive_emojis:
            return True
        else:
            return False

    @staticmethod
    def contains_emoji(text):
        p = re.compile("[:].*[:]")
        return re.findall(p, text)


    @staticmethod
    def contains_user(text):
        p = re.compile("[<@].*[>]")
        return re.findall(p, text)
