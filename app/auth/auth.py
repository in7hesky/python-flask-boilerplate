from .. import bcrypt
from flask import render_template, url_for, redirect
from . import auth_bp
from .forms import LoginForm, RegisterForm
from ..models import db, User

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password_hash=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("auth_bp.login"))
        
    return render_template("register.html", form=form)