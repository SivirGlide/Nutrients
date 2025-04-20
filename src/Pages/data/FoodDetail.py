from flask import render_template


def get_food_detail(food_id):
    return render_template('food-detail.html', food_id=food_id)