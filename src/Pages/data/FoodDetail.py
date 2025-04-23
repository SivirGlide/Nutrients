import requests
from flask import render_template

def get_food_detail(food_id, food_service):
    food_object = food_service.get_food_by_id(food_id)
    if food_object is None:
        food_data = "Couldn't find food with the specified id"
    else:
        food_data = food_object.get_nutrients()
    return render_template('food-detail.html', food_data=food_data)