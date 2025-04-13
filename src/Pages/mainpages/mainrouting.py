from flask import Blueprint

from src.Pages.mainpages.Dashboard import getDashboard
from src.Pages.mainpages.about import getAbout
from src.Pages.mainpages.landing import getLandingPage

mainbp = Blueprint('main', __name__)
@mainbp.route('/')
def landing():
    return getLandingPage()

@mainbp.route('/dashboard')
def dashboard():
    return getDashboard()

@mainbp.route('/about')
def about():
    return getAbout()