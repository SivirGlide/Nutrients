from flask import Blueprint, session, redirect

from src.Pages.data.Analysis import get_analysis
from src.Pages.data.FoodDetail import get_food_detail
from src.Pages.data.FoodSearch import get_foods
from src.Pages.data.Meals import get_meals
from src.Pages.data.Profile import get_profile


def register_dashboard_routing(app, food_service):
    dashbp = Blueprint('data', __name__, url_prefix='/dashboard')

    @dashbp.route('/meals', methods=['GET'])
    def meals():
        if not session.get('uuid'):
            return redirect('auth/signin')
        return get_meals()

    @dashbp.route('/profile', methods=['GET'])
    def profile():
        if not session.get('uuid'):
            return redirect('auth/signin')
        return get_profile()

    @dashbp.route('/analysis', methods=['POST'])
    def analysis():
        if not session.get('uuid'):
            return redirect('auth/signin')
        return get_analysis()

    @dashbp.route('/find-foods', methods=['GET', 'POST'])
    def find_foods():
        if not session.get('uuid'):
            return redirect('auth/signin')
        return get_foods(food_service)

    @dashbp.route('/find-foods/<food_id>', methods=['GET'])
    def food_detail(food_id):
        return get_food_detail(food_id)


    app.register_blueprint(dashbp)