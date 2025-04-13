from flask import Blueprint

from src.Pages.auth.Signup import getSignUp
from src.Pages.auth.Signin import getSignIn

authbp = Blueprint('auth', __name__, url_prefix='/auth')

@authbp.route('/signup', methods=['GET', 'POST'])
def signup():
    return getSignUp()

@authbp.route('/signin', methods=['GET', 'POST'])
def signin():
    return getSignIn()