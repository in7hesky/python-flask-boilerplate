### Project Description ###

This is an example of some boilerplate code which can be used as a base for creating flask web apps.

It supports flask's blueprints, dynamic configuration for different environments of choice and provides an implementation of basic authentication system.

The development environment is preconfigured to run debug toolbar extension by default.

List of main tools and libraries used:
- flask
- sqlite
- sqlalchemy
- dynaconf
- wtforms
- flask-login
- bootstrap5
- bcrypt

You can run the app in a docker container using `Dockerfile` provided or proceed with the instructions below to set it up by yourself.
## Prerequisites

Install python manually or let it be chosen by [pyenv](https://github.com/pyenv/pyenv) if you've got one (see `.python-version` file).

After that you just run:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Now set some environment variables, for **Linux** (dev mode) it works like that:
```
export FLASK_APP=app.py
export FLASK_ENV=development
```
You'll also need to set a `SECRET_KEY`. You may place it inside `config` folder in `.secrets.toml` file with such content:
```
[default]
SECRET_KEY="SOME_SECRET_SEQUENCE_HERE"
```
Now you just casually run the app with the command below:
```
flask run
```
If you wish to access your app with some other device by **LAN**, you may need to include an option for that feature:
```
flask run --host=0.0.0.0
```

## Running the app

After the app has started, the sqlite database file is created (`instance` folder).

You may open your browser and get to the app's homepage using `127.0.0.1:5000` ip address (default port).

To access the app via other device by **LAN**, you should use the host's local ip address (`192.168.*.*`).

The authentication pages are located on `/register` and `/login` endpoints.

*The auth system was built for learning purposes. Though it implements some data validation, the app by no means is considered ready to be hosted publicly.*
