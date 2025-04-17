from datetime import timedelta

from flask import Flask
from supabase import create_client
import os
from flask_session import Session

from config import SECRET_KEY, SUPABASE_URL, SUPABASE_KEY
from src.Pages.auth.authrouting import register_auth_routes
from src.Pages.mainpages.mainrouting import register_main_routes
from src.services.ServiceFactory import init_services


#Application factory should be made here, instead of using the app globally this makes it into a function.

def create_app(test_config=None):
    #create the flask instance providing it with location
    app = Flask('Nutrients', instance_relative_config=True, template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        SUPABASE_URL = SUPABASE_URL,
        SUPABASE_KEY = SUPABASE_KEY
    )


    app.config.from_mapping(test_config)

    #connect to supabase with config keys
    if app.config['SUPABASE_URL'] and app.config['SUPABASE_KEY']:
        app.supabase = create_client(
            app.config['SUPABASE_URL'],
            app.config['SUPABASE_KEY']
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #use if suspect an issue with the blueprints
    @app.route('/direct')
    def test():
        return "Direct routing test page"

    # I tried putting this configuration in the config.py file, but it returned saying tha values were null
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    #register the services and inject into routes
    services = init_services(app)
    register_auth_routes(app, services['auth_service'])
    register_main_routes(app, services['food_service'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)