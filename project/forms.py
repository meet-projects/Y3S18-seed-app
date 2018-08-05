from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(Form):
	displayname = StringField('Display Name', validators=[DataRequired(), Length(max=40)])
	username = StringField('Username', validators=[DataRequired(), Length(max=16)])
	password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
	confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=40)])


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

class PostForm(Form):
	title = StringField('Title', validators=[DataRequired()])
	text = TextAreaField('Text', validators=[DataRequired()])
	art_url = TextAreaField('Art URL', validators=[DataRequired()])

class AddArtForm(Form):
    art_url = StringField('ArtUrl', validators = [DataRequired()])

class ProfilePicForm(Form):
	profile_pic_url = StringField('URL', validators = [DataRequired()])

class ProfileBioForm(Form):
	profile_bio = StringField('Change Bio', validators = [DataRequired()])	    
     

