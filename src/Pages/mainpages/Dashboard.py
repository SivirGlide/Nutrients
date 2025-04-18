from flask import render_template, request, session, redirect


def getDashboard(food_service):
    if not session.get('uuid'):
        return redirect('auth/signin')

    if request.method == "GET":
        return render_template('dashboard.html')
    if request.method == "POST":
        return render_template('dashboard.html')