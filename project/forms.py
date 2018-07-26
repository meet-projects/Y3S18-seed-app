from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    number = StringField('Phone')
    name = StringField('Name')
    name1 = StringField('Name1')
    name2 = StringField('Name2')
    phone = StringField('Num')
    phone1 = StringField('Num')
    phone2 = StringField('Num')



class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

