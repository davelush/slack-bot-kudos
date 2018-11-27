# -*- coding: utf-8 -*-

import json
from flask import Flask, request, make_response, render_template
from slack_bot import bot
from kudos.sentiment import Sentiment
import psycopg2

# TODO go back and review the source code of the original Slack project for ideas
app = Flask(__name__)
postgres_connection = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres"
)
pyBot = bot.Bot(app.logger, postgres_connection)
slack = pyBot.client


def _event_handler(event_type, slack_event):
    # team_id = slack_event["team_id"]
    app.logger.info(f"{event_type} and body [{slack_event}]")

    if event_type == "message":
        text = slack_event["event"].get("text")
        channel_id = slack_event["event"].get("channel")
        sentiment = Sentiment()
        if sentiment.contains_emoji(text) and sentiment.contains_user(text):
            print(f"found an emoji and a user in : {text}")
            emojis = sentiment.contains_emoji(text)
            users = sentiment.contains_user(text)
            if sentiment.is_positive_emoji(emojis[0]):
                pyBot.give_kudos(emojis[0], users[0], channel_id)

        return make_response("Updated kudos status and sent messages", 200)
        # TODO probably want an emoji matcher and a findall to separate check from get
        # TODO same thing on users
    # elif event_type == "app_mention":
    #     user_id = slack_event["event"].get("user")
    #     channel_id = slack_event["event"].get("channel")
    #     # pyBot.auth("chat.postMessage")
    #     pyBot.send_quote_message(channel_id)
    #     return make_response("Sent a simple DM back to the person who mentioned me", 200,)
    elif event_type == "reaction_removed":
        return make_response("Not yet implemented", 200, )
    elif event_type == "emoji_changed":
        return make_response("Not yet implemented", 200, )

    message = "You have not added an event handler for the %s" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/install", methods=["GET"])
def pre_install():
    """This route renders the installation page with 'Add to Slack' button."""
    # Since we've set the client ID and scope on our Bot object, we can change
    # them more easily while we're developing our app.
    client_id = pyBot.oauth["client_id"]
    scope = pyBot.oauth["scope"]
    return render_template("install.html", client_id=client_id, scope=scope)


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    # FIXME OAuth is not working smoothly
    """
    This route is called by Slack after the user installs our app. It will
    exchange the temporary authorization code Slack sends for an OAuth token
    which we'll save on the bot object to use later.
    To let the user know what's happened it will also render a thank you page.
    """
    # Let's grab that temporary authorization code Slack's sent us from
    # the request's parameters.
    code_arg = request.args.get('code')
    # The bot's auth method to handles exchanging the code for an OAuth token
    pyBot.auth(code_arg)
    return render_template("thanks.html")


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    # Echo Slack's challenge when you subscribe to events
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    # Verify it's actually Slack sending us events
    if pyBot.verification != slack_event.get("token"):
        message = f"Invalid Slack verification token: {slack_event['token']} pyBot has: {pyBot.verification}"
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    # Handle any events correctly
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # Canned response for events we're not subscribed to
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids you're looking for.", 404,
                         {"X-Slack-No-Retry": 1})


if __name__ == '__main__':
    app.run(debug=True, port=8765)
