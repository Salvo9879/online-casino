
# Import Internal modules
from .databases import Users
from .helpers import iso_dt


# Import External modules
from wtforms.validators import ValidationError
import dateutil.parser as parser

import datetime


class ExistenceQuery(object):
    def __init__(self, type_=None, message=None):
        if type_ is None:
            raise AttributeError('Parameter \'type_\' can not be equal to None')
        if type_ not in ['username', 'email']:
            raise AttributeError('Parameter \'type_\' must either be equal to \'username\' or \'email\'')
        self.type_ = type_

        if not message:
            message = f"A user with this {type_} already exists."
        self.message = message

    def __call__(self, _, field):
        if self.type_ == 'username':
            user_query = Users.query.filter_by(username=field.data).first()
        if self.type_ == 'email':
            user_query = Users.query.filter_by(email=field.data).first()

        if user_query is not None:
            raise ValidationError(self.message)
        
class AgeLimit(object):
    def __init__(self, message=None):
        if not message:
            message = 'You must be 13 years or older to access our services.'
        self.message = message

    def __call__(self, _, field):
        birth_year = parser.parse(str(field.data)).year
        now_year = iso_dt().year
        age = now_year - birth_year

        if age < 13:
            raise ValidationError(self.message)

class VerifyUser(object):
    def __init__(self, message=None) -> None:
        if not message:
            message = 'Password or username is incorrect.'
        self.message = message

    def __call__(self, form, field):
        user_query = Users.query.filter_by(email=field.data).first()

        if user_query is None or not user_query.verify_password(form.password.data):
            raise ValidationError(self.message)