from flask import render_template


def get_meals():
    return render_template('meals.html')