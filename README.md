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

## Prerequisites
The app was built using `python 3.10.3`. You can install python manually or use pyenv so it will autodetect python's version.

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
Now you should be able to run the app using `flask run` command in your terminal.

## Running the app

After the app has started, the sqlite database file is created (`instance` folder).

You may open your browser and get to the app's homepage using `127.0.0.1:5000` ip address (default port).

The authentication pages are located on `/register` and `/login` endpoints.

*This auth system was built for learning purposes. Though it provides data validation, it doesn't consider the requests amount.
Therefore the app should not be hosted publicly in it's native state.*

