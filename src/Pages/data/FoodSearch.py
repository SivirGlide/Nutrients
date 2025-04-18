from flask import render_template


def get_foods():
    return render_template('food-lookup.html')