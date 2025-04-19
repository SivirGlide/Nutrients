from flask import render_template

#Green colour scheme
def get_foods():
    return render_template('food-lookup.html')