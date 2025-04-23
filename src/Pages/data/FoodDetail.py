import requests
from flask import render_template


def get_food_detail(food_id, food_service):
    food_object = food_service.get_food_by_id(food_id)
    API_KEY = 'rCAH4V3PHkLLZ99aoLNjYhMBe5a6ASmpn9D6twWc'
    temp_food_dict = {}
    response = requests.get(
        f'https://api.nal.usda.gov/fdc/v1/food/{food_id}?format=full&api_key={API_KEY}')
    food_data = response.json()
    for item in food_data['foodNutrients']:
            if 'amount' in item:
             temp_food_dict[f'{item['nutrient']['name']}'] = f'{item['amount']}{item['nutrient'].get('unitName', '')}'
            if 'value' in item:
                temp_food_dict[f'{item['nutrient']['name']}'] = f'{item['value']}{item['nutrient'].get('unitName', '')}'
            else:
                pass
    print(temp_food_dict)
    return render_template('food-detail.html', food_id=temp_food_dict)