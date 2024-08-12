from .. import bcrypt, login_manager
from flask import render_template, url_for, redirect
from . import auth_bp
from .forms import LoginForm, RegisterForm
from ..models import db, User
from flask_login import login_required, login_user, logout_user
import flask_login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=flask_login.current_user.username)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for("auth_bp.dashboard"))
    
    return render_template("login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))

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