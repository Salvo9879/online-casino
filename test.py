from gambol.databases import Users
from app import app

with app.app_context():
    user_query = Users.query.filter_by(username='Salvo989').first()
    print(user_query is not None)