# -*- coding: utf-8 -*-
import os
import sys
from argparse import ArgumentParser

import psycopg2
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from org.davelush.slack_bot import bot
from org.davelush.slack_bot.slack_event_handler import SlackEventHandler
from org.davelush.slack_bot.slack_install_handler import SlackInstallHandler
from org.davelush.slack_bot.slack_post_install_handler import SlackPostInstallHandler


def parse_cli_args(command_line, environment):
    parser = ArgumentParser()

    parser.add_argument(
        "--postgres-host",
        action="store_true",
        default=environment.get("POSTGRES_HOST", "localhost"),
        help="Postgres host"
    )
    parser.add_argument(
        "--postgres-port",
        action="store_true",
        default=int(environment.get("POSTGRES_PORT", 5432)),
        help="Postgres host's port"
    )
    parser.add_argument(
        "--postgres-db",
        action="store_true",
        default=environment.get("POSTGRES_DB", "metrics"),
        help="Postgres DB"
    )
    parser.add_argument(
        "--postgres-schema",
        action="store_true",
        default=environment.get("POSTGRES_SCHEMA", "kudosbot"),
        help="Postgres DB's schema"
    )
    parser.add_argument(
        "--postgres-user",
        action="store_true",
        default=environment.get("POSTGRES_USER", None),
        help="Postgres DB's schema"
    )
    parser.add_argument(
        "--postgres-pass",
        action="store_true",
        default=environment.get("POSTGRES_PASS", None),
        help="Postgres password"
    )

    arguments = parser.parse_args(command_line)

    return arguments


def setup():
    args = parse_cli_args(sys.argv[1:], os.environ)
    postgres_connection = psycopg2.connect(
        host=args.postgres_host,
        port=args.postgres_port,
        dbname=args.postgres_db,
        user=args.postgres_user,
        password=args.postgres_pass
    )
    py_bot = bot.Bot(postgres_connection)

    app = Flask(__name__)
    CORS(app, resources={'/*': {'origins': '*'}})
    api = Api(app, catch_all_404s=True)
    api.add_resource(SlackEventHandler, '/listening', resource_class_kwargs={'py_bot': py_bot})
    api.add_resource(SlackPostInstallHandler, '/thanks', resource_class_kwargs={'py_bot': py_bot})
    api.add_resource(SlackInstallHandler, '/thanks', resource_class_kwargs={'py_bot': py_bot})
    return app, api


flask_app, flask_api = setup()

if __name__ == '__main__':
    flask_app.run(debug=True, port=8765)
