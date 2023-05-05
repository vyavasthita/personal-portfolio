from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class UserRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField('Password Repeat', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')