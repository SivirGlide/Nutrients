from flask import Blueprint, session, redirect
from src.Pages.data.FoodDetail import get_food_detail
from src.Pages.data.FoodSearch import get_foods


def register_dashboard_routing(app, food_service):
    dashbp = Blueprint('data', __name__, url_prefix='/dashboard')

    @dashbp.route('/find-foods', methods=['GET', 'POST'])
    def find_foods():
        if not session.get('uuid'):
            return redirect('auth/signin')
        return get_foods(food_service)

    @dashbp.route('/find-foods/<food_id>', methods=['GET'])
    def food_detail(food_id):
        return get_food_detail(food_id,food_service)


    app.register_blueprint(dashbp)