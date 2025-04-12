from flask import Flask
from supabase import create_client
import os



#Application factory should be made here, instead of using the app globally this makes it into a function.

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SUPABASE_URL = '',
        SUPABASE_KEY = ''
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

        if app.config['SUPABASE_URL'] and app.config['SUPABASE_KEY']:
            app.supabase = create_client(
                app.config['SUPABASE_URL'],
                app.config['SUPABASE_KEY']
            )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return "Home Page"

    return app