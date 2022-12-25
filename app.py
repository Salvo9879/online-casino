
# Import internal modules
from gambol import db, Users
from gambol.routes import credentials, api, errorhandlers

# Import external modules
from flask import Flask
from flask_login import LoginManager


# Define application
app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = 'e18ac63530ab499caac5d3c171edd5e2b0925bd68935f46a65258507b6dfe8e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Define database
db.init_app(app)

# Define LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Register routing blueprints blueprints
app.register_blueprint(credentials)
app.register_blueprint(api)
app.register_blueprint(errorhandlers)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )