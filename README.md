# Slack Bot Sandbox

This is my sandbox for playing around with creating a Slack bot. As a starting point I've used the [Slack Python Onboarding Tutorial](https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/README.md#pythonboarding-bot) which gives a good set of initial constructs along with guidance on setup. Plans from here are;

- [x] Get to grips with the incoming events and how to generate outbound messages
- [x] Set up a few fun interactions for the bot
- [x] Add some test coverage via [pytest](https://docs.pytest.org/en/latest/)
- [ ] Watch for positive emojis in relation to people
- [ ] Create a Dockerfile so that it can be deployed in a K8s cluster

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
2. Update the Request URL in the Event Subscriptions section of your Slack app configuration 
    - `http://abcdef01.ngrok.io/listening` — Don't forget to add listening to the end of the url
    - `docker run --rm -it -p 8080:8080 $IMAGE_ID_FROM_ABOVE`
3. Run your application on 8765 locally

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
