from flask import render_template, request, flash

from src.Pages.mainpages.mainrouting import dashboard
from src.services.auth_services.AuthService import AuthService


def getSignUp():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        #Store the form data in an array and parse to authentication service
        signupform = {
            "Name": request.form['username'],
            "Email": request.form['email'],
            "Password": request.form['password'],
            "ConfirmPassword": request.form['confirm-password']
        }
        #submit form to validation service and flash errors if there are any
        attemptSignUp = AuthService(signupform)
        is_valid, errors = attemptSignUp.signup()
        if not is_valid:
            for error in errors:
                flash(error, 'error')
                return render_template('signup.html')
        return render_template('dashboard.html')