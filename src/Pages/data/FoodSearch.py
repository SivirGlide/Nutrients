from flask import render_template, request


#Green colour scheme
def get_foods(food_service):
    if request.method == 'GET':
        food_id = request.args.get('id')
        if food_id is None:
            return render_template('food-lookup.html')
        response = food_service.post_to_eaten(food_id)
        return render_template('food-lookup.html')

    if request.method == 'POST':
        response = food_service.get_food_list(request.form.get('Search-for-food'))
        item_list = []
        for item in response:
            item_list.append(item)
        return render_template('food-lookup.html',items=item_list)