# Kudos Slack Bot

This is started as a sandbox for playing around with creating a Slack bot. As I've become more comfortable with the programming model it's morphing into a bot for both receiving and giving kudos (regular peer feedback) as a Slack user. I've used the [Slack Python Onboarding Tutorial](https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/README.md#pythonboarding-bot) which gives a good set of initial constructs along with guidance on setup.

If you want to follow what I'm up to now and next there is a [Trello Board](https://trello.com/b/7GD4f1QM/kudos-slack-bot)

## Getting Started

These instructions will get you a copy of the application up and running on your local machine for development purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3.7+
A Slack app configured in your workspace
```

### Running locally

1.Set the following environment variables
```commandline
export CLIENT_ID=<client id from bot OAuth settings in Slack>
export CLIENT_SECRET=<client secret from bot OAuth settings in Slack>
export BOT_TOKEN=<Temporary workaround. Bot-token from Slack>
export VERIFICATION_TOKEN=???
``` 
2. Run ngrok
    - `ngrok http 8765`
3. Update the Request URL in the Event Subscriptions section of your [Slack App](https://api.slack.com/apps) configuration 
    - `http://abcdef01.ngrok.io/listening` — Don't forget to add listening to the end of the url
    - `docker run --rm -it -p 8080:8080 $IMAGE_ID_FROM_ABOVE`
4. Set an environment variable of `$BOT_TOKEN=abcdef01`. This is the Bot User OAuth Access Token from your Slack App configuration. This is a temporary workaround as I'm having trouble getting the OAuth flow working smoothly.
5. Run your application on 8765 locally

## Running the tests

Not a lot of coverage. From the root directory run
```
pytest
```

## Deployment

Not yet added. Base `Dockerfile` is available but untested

## Built With

* [Flask](https://github.com/pallets/flask) - The Python micro framework for building web applications.
* [Python SlackClient](https://github.com/slackapi/python-slackclient) - Slack Developer Kit for Python.

## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/davelush/slack-bot-sandbox/tags).

## Authors

Here is a list of [contributors](https://github.com/davelush/slack-bot-sandbox/graphs/contributors) who participated in this project.



adding a test commit right here at the bottom