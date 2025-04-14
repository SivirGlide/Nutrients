from flask import Blueprint

from src.Pages.auth.Signup import getSignUp
from src.Pages.auth.Signin import getSignIn


def register_auth_routes(app,auth_service):
    authbp = Blueprint('auth', __name__, url_prefix='/auth')

    @authbp.route('/signup', methods=['GET', 'POST'])
    def signup():
        return getSignUp(auth_service)

    @authbp.route('/signin', methods=['GET', 'POST'])
    def signin():
        return getSignIn(auth_service)

    app.register_blueprint(authbp)