
# Import internal modules
from .helpers import iso_dt
from .exceptions import FailedToCreateUser

# Import external modules
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash

# Define the sqlalchemy integration
db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)

    birthdate = db.Column(db.DateTime, nullable=False)

    dt_created = db.Column(db.DateTime, nullable=False, default=iso_dt())
    dt_modified = db.Column(db.DateTime, nullable=False, default=iso_dt())

    password_hashed = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"[{self.id}] - {self.forename} {self.surname} | email/{self.email}, username/{self.username} | birthdate/{self.birthdate} | dt_created/{self.dt_created}, dt_modified/{self.dt_modified} | PWD (hash) : {self.password_hashed} ->"

    @property
    def password(self):
        raise AttributeError('Property \'password\' is not readable!')

    @password.setter
    def password(self, password):
        self.password_hashed = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hashed, password)

def create_account(details: dict):
    u = Users()
    u.forename = details['forename']
    u.surname = details['surname']
    u.username = details['username']
    u.email = details['email']
    u.birthdate = details['birthdate']
    u.password = details['password_beta']

    try:
        db.session.add(u)
        db.session.commit()
    except:
        FailedToCreateUser('Failed to commit user to the user database. User was not created.')

def auto_login_user(user_password, user_email, redirection_url):
    user_query = Users.query.filter_by(email=user_email).first()

    if not user_query.verify_password(user_password):
        raise FailedToCreateUser('The server successfully created the account, but failed to sign them in under correct credentials.')
    return redirect(redirection_url)