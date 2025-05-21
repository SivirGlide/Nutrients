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
    food_list = []
    if food_list is None:
        food_list = "Looks like you haven't eaten today, Add a food to view it here!"
    #if meals list has values, get the basic nutritional info of those meals

    #if meals list has values, get the advanced nutritional info of those meals

    #if meals list has values, get the graph info of those meals

    if request.method == "GET":
        return render_template('dashboard.html', user=user,time=time, meal_list = food_list)

    if request.method == "POST":
        return render_template('dashboard.html')