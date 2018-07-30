from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(Form):
    email = StringField('Email Address', validators=[DataRequired(), Length(max=40)])
    name = StringField('Full Name', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(Form):
    email = StringField('Email Address', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

