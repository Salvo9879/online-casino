
# Import internal modules
from .helpers import iso_dt

# Import external modules
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Define the sqlalchemy integration
db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

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