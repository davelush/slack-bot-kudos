import logging
from unittest import TestCase
from org.davelush.slack_bot.logging_setup import initialise_logging


class TestLoggingSetup(TestCase):

    def test_default_logging_level(self):
        initialise_logging(None)
        logger = logging.getLogger()
        self.assertEqual(logger.level, logging.INFO)

    def test_set_logging_level(self):
        initialise_logging(logging.DEBUG)
        logger = logging.getLogger()
        self.assertEqual(logger.level, logging.DEBUG)
