from flask import render_template
from . import auth_bp
from .forms import LoginForm, RegisterForm

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return "LoginPage"

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return "RegisterPage"