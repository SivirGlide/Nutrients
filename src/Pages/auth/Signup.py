from flask import render_template, request, flash, redirect


def getSignUp(auth_service):
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        #Store the form data in an array and parse to authentication service
        signupform = {
            "name": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password'],
            "confirmPassword": request.form['confirm-password']
        }
        #submit form to validation service and flash errors if there are any
        is_valid, errors = auth_service.signup(signupform)
        if not is_valid:
            for error in errors:
                flash(error, 'error')
                return render_template('signup.html')
        return redirect('/dashboard')