import datetime

from flask import render_template, request, session, redirect

def getDashboard(food_service, user_service):
    if not session.get('uuid'):
        return redirect('auth/signin')

    #get the username and time of day
    user = user_service.get_name({'uuid': session['uuid']})
    time = datetime.datetime.now()
    time = time.time()

    # KISS
    if time.hour <= 11:
        time = 'Morning'
    elif time.hour <= 17:
        time = 'Afternoon'
    elif time.hour <= 23:
        time = 'Evening'

    #get all meals eaten today based on uuid, or return null
    food_list = food_service.get_eaten_foods_by_session()
    #if meals list has values, get the basic nutritional info of those meals
    food_nutrient_list = food_service.get_food_id_list()

    nutrient_list = {
        "Calories": 0,
        "Fat": 0,
        "Carbohydrates": 0,
        "Sugar": 0,
        "Protein": 0,
        "Fibre": 0,
    }

    for item in food_nutrient_list:
        temp = item.get('Nutrients')

        for key in nutrient_list:
            try:
                value = temp.get(key, 0)
                # Round to 2 decimal places as we add
                nutrient_list[key] = round(nutrient_list[key] + float(value), 2)
            except (ValueError, TypeError):
                print(f"Warning: Could not convert {key} value '{temp.get(key)}' to number")
                continue

    print(nutrient_list)
    for nutrient in nutrient_list:
        print(nutrient, nutrient_list[nutrient])

    if request.method == "GET":
        return render_template('dashboard.html', user=user,time=time, meal_list = food_list, nutrient_list = nutrient_list)

    if request.method == "POST":
        return render_template('dashboard.html')