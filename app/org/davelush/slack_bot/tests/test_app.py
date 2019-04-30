import os
import sys
from unittest import TestCase
from unittest.mock import patch


class TestApp(TestCase):

    def tearDown(self):
        if os.environ.get("POSTGRES_HOST"):
            del os.environ["POSTGRES_HOST"]

    def test_config_defaults(self):
        with patch("psycopg2.connect") as mock_psycopg2_connect:

            from org.davelush.slack_bot.app import parse_cli_args
            args = parse_cli_args(sys.argv[1:], os.environ)
            assert args.postgres_host == "localhost"
            assert args.postgres_port == 5432
            assert args.postgres_db == "metrics"
            assert args.postgres_schema == "kudosbot"
            assert args.client_id == "id"
            assert args.client_secret == "secret"
            assert args.bot_token == "bot_token"
            assert args.postgres_user is None
            assert args.postgres_pass is None

    def test_config_env_vars(self):
        with patch("psycopg2.connect") as mock_psycopg2_connect:
            os.environ["POSTGRES_HOST"] = "some.random.host"
            from org.davelush.slack_bot.app import parse_cli_args
            args = parse_cli_args(sys.argv[1:], os.environ)
            assert args.postgres_host == "some.random.host"

    def test_setup(self):
        with patch("psycopg2.connect") as mock_psycopg2_connect:
            mock_psycopg2_connect.return_value = None
            from org.davelush.slack_bot.app import setup
            flask_app, flask_api = setup()
            assert flask_app is not None
            assert flask_api is not None
            assert len(flask_api.endpoints) > 0
