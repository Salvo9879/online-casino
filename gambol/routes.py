
# Import internal modules
from .forms import SignupForm, LoginForm
from .databases import Users, create_account, auto_login_user

# Import external modules
from flask import Blueprint, render_template, redirect, url_for, flash, get_flashed_messages
from flask_login import login_user, logout_user, current_user

# Define application blueprints
credentials = Blueprint('credentials', __name__)
errorhandlers = Blueprint('errorhandlers', __name__)
api = Blueprint('api', __name__)

class Credentials():
    @credentials.route('/signup')
    def signup():
        if current_user.is_anonymous:
            signup_form = SignupForm()
            errors = {}

            if get_flashed_messages():
                errors = get_flashed_messages()[0]

            return render_template('signup.html', signup_form=signup_form, errors=errors)
        return redirect(url_for('dashboard'))

    @credentials.route('/login')
    def login():
        if current_user.is_anonymous:
            login_form = LoginForm()
            errors = {}

            if get_flashed_messages():
                errors = get_flashed_messages()[0]

            return render_template('login.html', login_form=login_form, errors=errors)
        return redirect(url_for('dashboard'))

    @credentials.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('credentials.login'))

class Api():
    @api.route('/api/44195', methods=['POST'])
    def api_44195():
        signup_form = SignupForm()

        if signup_form.validate_on_submit():
            create_account(signup_form.data)
            auto_login_user(signup_form.email.data, signup_form.password_beta.data, url_for('/dashboard'))

        flash(signup_form.errors)
        return redirect(url_for('credentials.signup'))

    @api.route('/api/51461', methods=['POST'])
    def api_51461():
        login_form = LoginForm()

        if login_form.validate_on_submit():
            user_query = Users.query.filter_by(email=login_form.email.data).first()

            login_user(user_query)
            return redirect(url_for('/dashboard'))
        
        flash(login_form.errors)
        return redirect(url_for('credentials.login'))