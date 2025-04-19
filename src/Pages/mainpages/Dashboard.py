from flask import render_template, request, session, redirect

def getDashboard(food_service):
    if not session.get('uuid'):
        return redirect('auth/signin')

    #get the username and time of day
    user = 'Arizona'
    time = 'Evening'
    #get all meals eaten today, or return null

    #if meals list has values, get the basic nutritional info of those meals

    #if meals list has values, get the advanced nutritional info of those meals

    #if meals list has values, get the graph info of those meals

    if request.method == "GET":
        return render_template('dashboard.html', user=user,time=time)

    if request.method == "POST":
        return render_template('dashboard.html')