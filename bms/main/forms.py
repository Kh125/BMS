from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from bms.models import User

class LoginForm(FlaskForm):
  email = StringField('Email',validators = [DataRequired()])
  password = PasswordField('Password',validators = [DataRequired(),Length(min = 8)])
  submit = SubmitField('Login')

class RegisterForm(FlaskForm):
  username = StringField('Username',validators = [DataRequired(),Length(min=5)])
  email = StringField('Email',validators = [DataRequired()])
  password = PasswordField('Password',validators = [DataRequired(),Length(min = 8)])
  confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')])
  submit = SubmitField('Register')

  def validate_username(self,username):
    user=User.query.filter_by(name=username.data).first()
    if user:
      raise ValidationError('This username already exists.Try another!')

  def validate_email(self,email):
    user=User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('This email already exists.Try another!')