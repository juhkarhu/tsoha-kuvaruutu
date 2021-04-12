from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from kuvaruutu.models import User

class RegistrationForm(FlaskForm): 
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('ConfirmPassword', 
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is taken. Please choose a different one.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    file = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


# id SERIAL PRIMARY KEY, 
# content TEXT, 
# comment_id INTEGER REFERENCES posts, 
# user_id INTEGER REFERENCES users,  
# sent_at TIMESTAMP,
# visible INTEGER DEFAULT 1