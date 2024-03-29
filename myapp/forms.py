from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class SignupForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    password2=PasswordField('Repeat Password',validators=[DataRequired()])
    accept_rules=BooleanField('I accept the site rules',validators=[DataRequired()])
    submit=SubmitField('Register')
    