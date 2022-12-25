from gambol import Users
from app import app

with app.app_context():
    print(Users.query.filter_by(id=728).first())