# -*- coding: utf-8 -*-
import psycopg2
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from slack_bot import bot
from slack_bot.slack_event_handler import SlackEventHandler
from slack_bot.slack_install_handler import SlackInstallHandler
from slack_bot.slack_post_install_handler import SlackPostInstallHandler


def setup():
    postgres_connection = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="postgres"
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
