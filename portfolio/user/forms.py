from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class UserRegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password_repeat = PasswordField('password_repeat', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('register')