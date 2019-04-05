FROM python:3.7-alpine

ENV PATH="${PATH}:/root/.local/bin"
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --user pipenv

# Following env vars required for pipenv
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY README.md setup.py Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pipenv install && pipenv run python3 setup.py install

COPY . /app

ENTRYPOINT [ "pipenv", "run", "python3", "-m", "slack_bot" ]