from flask import render_template
from flask_restful import Resource


def pre_install(py_bot):
    """This route renders the installation page with 'Add to Slack' button."""
    # Since we've set the client ID and scope on our Bot object, we can change
    # them more easily while we're developing our app.
    client_id = py_bot.oauth["client_id"]
    scope = py_bot.oauth["scope"]
    return render_template("install.html", client_id=client_id, scope=scope)


class SlackInstallHandler(Resource):

    def __init__(self, **kwargs):
        self.py_bot = kwargs.get('py_bot')

    def get(self):
        return pre_install(self.py_bot)
