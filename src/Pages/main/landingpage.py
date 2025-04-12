from flask import render_template

from .mainpages import mainbp

@mainbp.route('/')
def landing():
    return render_template('landing.html')