
# Import internal modules
from .validators import ExistenceQuery, AgeLimit, VerifyUser

# Import external modules
from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, EmailField, PasswordField
from wtforms.validators import InputRequired, email, EqualTo

class SignupForm(FlaskForm):
    forename = StringField(validators=[InputRequired(message='A forename is required.')])
    surname = StringField(validators=[InputRequired(message='A surname is required.')])

    birthdate = DateField(validators=[InputRequired(message='A birthdate is required.'), AgeLimit()])

    email = EmailField(validators=[InputRequired(message='A email is required.'), email(message='A valid email is required.'), ExistenceQuery(type_='email')])
    username = StringField(validators=[InputRequired(message='A username is required.'), ExistenceQuery(type_='username')])

    password_alpha = PasswordField(validators=[InputRequired(message='A password must be given.')])
    password_beta = PasswordField(validators=[InputRequired(), EqualTo('password_alpha', message='Both passwords must match.')])

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(message='A username is required'), VerifyUser()])
    password = PasswordField(validators=[InputRequired(message='A password must be given.')])