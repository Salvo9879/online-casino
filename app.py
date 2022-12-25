
# Import internal modules
from gambol import db, app_

# Import external modules
from flask import Flask


# Define application
app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = 'e18ac63530ab499caac5d3c171edd5e2b0925bd68935f46a65258507b6dfe8e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Define database
db.init_app(app)

# Register app_ blueprints
app.register_blueprint(app_)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )