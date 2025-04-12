from flask import Flask
from supabase import create_client
import os

from src.Pages.mainpages.mainrouting import mainbp


#Application factory should be made here, instead of using the app globally this makes it into a function.

def create_app(test_config=None):
    #create the flask instance providing it with location
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev',
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
            app.config['SUPABASE_URL'],
            app.config['SUPABASE_KEY']
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/direct')
    def hello():
        return "Test Direct Page"

    app.register_blueprint(mainbp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)