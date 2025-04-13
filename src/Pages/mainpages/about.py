from flask import render_template


def getAbout():
    return render_template('about.html')