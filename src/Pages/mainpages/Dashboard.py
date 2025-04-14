from flask import render_template


def getDashboard():
    return render_template('dashboard.html')