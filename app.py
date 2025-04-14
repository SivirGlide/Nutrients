from flask import Flask
from supabase import create_client
import os

from config import SECRET_KEY, SUPABASE_URL, SUPABASE_KEY
from src.Pages.auth.authrouting import register_auth_routes
from src.Pages.mainpages.mainrouting import mainbp
from src.services.ServiceFactory import auth_service

#Application factory should be made here, instead of using the app globally this makes it into a function.

def create_app(test_config=None):
    #create the flask instance providing it with location
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        SUPABASE_URL = '',
        SUPABASE_KEY = ''
    )

    #get basic config if custom one does not exist
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    #connect to supabase with config keys
    if app.config['SUPABASE_URL'] and app.config['SUPABASE_KEY']:
        app.supabase = create_client(
            SUPABASE_URL,
            SUPABASE_KEY
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/direct')
    def hello():
        return "Test Direct Page"

    register_auth_routes(app, auth_service)
    app.register_blueprint(mainbp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)