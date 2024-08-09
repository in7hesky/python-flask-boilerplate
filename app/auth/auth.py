from flask import render_template
from . import auth_bp
from .forms import LoginForm, RegisterForm

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)