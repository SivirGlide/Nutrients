from flask import render_template

#orange colour scheme
def get_meals():
    return render_template('meals.html')