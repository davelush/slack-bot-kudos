from flask import render_template, request
from flask_restful import Resource


def thanks(py_bot):
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
    py_bot.auth(code_arg)
    return render_template("thanks.html")


class SlackPostInstallHandler(Resource):

    def __init__(self, **kwargs):
        self.py_bot = kwargs.get('py_bot')

    def get(self):
        return thanks(self.py_bot)

    def post(self):
        return thanks(self.py_bot)
