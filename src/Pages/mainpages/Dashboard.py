from flask import render_template, request, session, redirect

def getDashboard(meal_service):
    if not session.get('uuid'):
        return redirect('auth/signin')

    #get the username and time of day
    user = 'Arizona'
    time = 'Evening'
    #get all meals eaten today based on uuid, or return null
    meal_list = meal_service.get_meals(session['uuid'])
    if meal_list is None:
        meal_list = "Looks like you haven't eaten today, Add a meal to view it here!"
    #if meals list has values, get the basic nutritional info of those meals

    #if meals list has values, get the advanced nutritional info of those meals

    #if meals list has values, get the graph info of those meals

    if request.method == "GET":
        return render_template('dashboard.html', user=user,time=time, meal_list = meal_list)

    if request.method == "POST":
        return render_template('dashboard.html')