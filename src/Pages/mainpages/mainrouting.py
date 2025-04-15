from flask import Blueprint

from src.Pages.mainpages.Dashboard import getDashboard
from src.Pages.mainpages.about import getAbout
from src.Pages.mainpages.landing import getLandingPage


def register_main_routes(app, food_service):
    mainbp = Blueprint('main', __name__)
    @mainbp.route('/')
    def landing():
        return getLandingPage()

    @mainbp.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return getDashboard(food_service)

    @mainbp.route('/about')
    def about():
        return getAbout()

    app.register_blueprint(mainbp)