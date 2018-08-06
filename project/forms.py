from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

