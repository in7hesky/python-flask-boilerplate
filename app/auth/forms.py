from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from ..models import User
from flask import flash

MIN_LENGTH = 4
MAX_LENGTH = 20

class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=MIN_LENGTH, max=MAX_LENGTH)
        ],
        render_kw={"placeholder": "Username"}
    )
    
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=MIN_LENGTH, max=MAX_LENGTH)
        ],
        render_kw={"placeholder": "Password"}
    )
    
    submit = SubmitField("Register")
    
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        
        if existing_user_username:
            error_message="Username already registered."
            flash(error_message)
            raise ValidationError(error_message)
        
class LoginForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Username"}
    )
    
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Password"}
    )
    
    submit = SubmitField("Login")
                