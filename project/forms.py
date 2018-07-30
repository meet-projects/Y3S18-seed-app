from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    number = StringField('Phone', validators=[DataRequired(), Length(max=40)])

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

class AddContactForm():
    name = StringField('name', validators=[DataRequired(), Length(max=40)])
    phone = StringField('phone', validators=[DataRequired(), Length(max=40)])
