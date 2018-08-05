from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    number = StringField('Phone', validators=[DataRequired(), Length(max=40)])
    booster_seat_id = StringField('booster_seat_id', validators=[DataRequired(), Length(max=40)])

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

class AddContactForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(max=40)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=40)])
    relation = StringField('Relation', validators=[DataRequired(), Length(max=40)])

