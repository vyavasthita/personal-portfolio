from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, DateField, EmailField,SubmitField
from wtforms.validators import DataRequired


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = EmailField('Email', validators= [DataRequired()])
    phone = StringField('Phone No', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Save')

