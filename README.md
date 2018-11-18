# Kudos Slack Bot

This is started as a sandbox for playing around with creating a Slack bot. As I've become more comfortable with the programming model it's morphing into a bot for both receiving and giving kudos (regular peer feedback) as a Slack user. I've used the [Slack Python Onboarding Tutorial](https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/README.md#pythonboarding-bot) which gives a good set of initial constructs along with guidance on setup. 

### What has been done?
- [x] Get to grips with the incoming events and how to generate outbound messages
- [x] Set up a few fun interactions for the bot (random Gonzo quotes as a starter)
- [x] Put a few basic [pytest](https://docs.pytest.org/en/latest/) tests in place (PyTest and Python are new to me)

### What is left to do?

- [ ] Identify messages with an emoji and a tagged person
- [ ] Identify that the emoji is associated with giving kudos
- [ ] Look at a Trello and GitHub integration. Be nice to link a kanban board with this
- [ ] Keep track of who has received what kudos (in memory initially)
- [ ] Stop people from giving themselves kudos
- [ ] Create a Dockerfile so that it can be deployed in a K8s cluster
- [ ] Persist this state to a DB

## Getting Started

These instructions will get you a copy of the application up and running on your local machine for development purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3.7+
A Slack app configured in your workspace
```

### Running locally

1. Run ngrok
    - `ngrok http 8765`
2. Update the Request URL in the Event Subscriptions section of your [Slack App](https://api.slack.com/apps) configuration 
    - `http://abcdef01.ngrok.io/listening` — Don't forget to add listening to the end of the url
    - `docker run --rm -it -p 8080:8080 $IMAGE_ID_FROM_ABOVE`
3. Set an environment variable of `$BOT_TOKEN=abcdef01`. This is the Bot User OAuth Access Token from your Slack App configuration. This is a temporary workaround as I'm having trouble getting the OAuth flow working smoothly.
4. Run your application on 8765 locally

## Running the tests

Not a lot of coverage. From the root directory run
```
pytest
```

## Deployment

Not yet added

## Built With

* [Flask](https://github.com/pallets/flask) - The Python micro framework for building web applications.
* [Python SlackClient](https://github.com/slackapi/python-slackclient) - Slack Developer Kit for Python.

## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/davelush/slack-bot-sandbox/tags).

## Authors

Here is a list of [contributors](https://github.com/davelush/slack-bot-sandbox/graphs/contributors) who participated in this project.
