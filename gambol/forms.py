
# Import internal modules
from .validators import ExistenceQuery, AgeLimit

# Import external modules
from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, EmailField, PasswordField
from wtforms.validators import InputRequired, email, EqualTo

class SignupForm(FlaskForm):
    forename = StringField(validators=[InputRequired()])
    surname = StringField(validators=[InputRequired()])

    birthdate = DateField(validators=[InputRequired(), AgeLimit()]) #! Create custom validator for age limit

    email = EmailField(validators=[InputRequired(), email(), ExistenceQuery(type_='email')])
    username = StringField(validators=[InputRequired(), ExistenceQuery(type_='username')])

    password_alpha = PasswordField(validators=[InputRequired()])
    password_beta = PasswordField(validators=[InputRequired(), EqualTo('password_alpha', message='Both passwords must match.')])