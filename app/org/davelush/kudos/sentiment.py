# -*- coding: utf-8 -*-
"""
Module for encapsulating the Sentiment class
"""
import logging
import re


#TODO it'd be good it this stored all emojis within a message and provided a score of positive / negative across all of
# them
#TODO the set of emojis should be configurable


class Sentiment(object):
    """
    Sentiment class finds emojis in a message and checks allows checking of whether an emoji is positive or not
    """
    def __init__(self):
        pass

    @staticmethod
    def is_positive_emoji(emoji):
        positive_emojis = [":star:",
                           ":star2:",
                           ":stars:",
                           ":cookie:",
                           ":chocfish:",
                           ":chocfish2:"]

        if emoji in positive_emojis:
            return True
        else:
            return False

    @staticmethod
    def get_positive_emojis(text):
        try:
            p = re.compile("[:][0-9aA-zZ]{1,9}[:]")
            emojis = re.findall(p, text)
        except:
            logging.warning(f"had a problem with regex on text [{text}]")
        finally:
            positive_emojis = []
            for emoji in emojis:
                if Sentiment.is_positive_emoji(emoji):
                    positive_emojis.append(emoji)
            if len(positive_emojis) > 0:
                return True, positive_emojis
            else:
                return False, positive_emojis


    @staticmethod
    def get_users(text):
        p = re.compile("<@[0-9aA-zZ]{9}>")
        result = re.findall(p, text)
        if len(result) > 0:
            return True, result
        else:
            return False, result
