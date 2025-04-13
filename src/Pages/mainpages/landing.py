from flask import render_template

def getLandingPage():
    return render_template("landing.html")