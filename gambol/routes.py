
# Import internal modules
from .forms import SignupForm

# Import external modules
from flask import Blueprint, render_template, redirect, url_for

# Define the routes blueprint
app_ = Blueprint('routes', __name__)

@app_.route('/')
def index():
    return

@app_.route('/signup', methods=['POST', 'GET'])
def signup():
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        pass
    print(signup_form.errors)
    return render_template('signup.html', signup_form=signup_form)