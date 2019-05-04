import os
import sys
from unittest import TestCase
from unittest.mock import patch

from org.davelush.slack_bot.app import parse_cli_args, setup


class TestApp(TestCase):

    def tearDown(self):
        if os.environ.get("POSTGRES_HOST"):
            del os.environ["POSTGRES_HOST"]

    def test_config_defaults(self):
        args = parse_cli_args(sys.argv[1:], os.environ)
        self.assertEqual(args.postgres_host, "localhost")
        self.assertEqual(args.postgres_port, 5432)
        self.assertEqual(args.postgres_db, "metrics")
        self.assertEqual(args.postgres_schema, "kudosbot")
        self.assertEqual(args.client_id, "id")
        self.assertEqual(args.client_secret, "secret")
        self.assertEqual(args.bot_token, "bot_token")
        self.assertIsNone(args.postgres_user)
        self.assertIsNone(args.postgres_pass)

    def test_config_env_vars(self):
        os.environ["POSTGRES_HOST"] = "some.random.host"
        args = parse_cli_args(sys.argv[1:], os.environ)
        self.assertEquals(args.postgres_host, "some.random.host")

    def test_setup(self):
        with patch("psycopg2.connect") as mock_psycopg2_connect:
            mock_psycopg2_connect.return_value = None
            flask_app, flask_api = setup()
            self.assertIsNotNone(flask_app)
            self.assertIsNotNone(flask_api)
            self.assertTrue(len(flask_api.endpoints) > 0)
