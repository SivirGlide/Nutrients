from flask import render_template, request


def getDashboard(food_service):
    if request.method == "GET":
        return render_template('dashboard.html')
    if request.method == "POST":
        food_data = request.form.to_dict()
        #call the food service
        is_valid, code = food_service.create_food(food_data)
        if not is_valid:
            print("Invalid food data" + code)
        else:
            print("Successfully created food data" + code)
        return render_template('dashboard.html')