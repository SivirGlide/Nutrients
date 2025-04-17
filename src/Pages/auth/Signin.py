from flask import render_template, request, flash, redirect

def getSignIn(auth_service):
    if request.method == 'GET':
        return render_template('signin.html')
    if request.method == 'POST':
        loginform = {
            "email": request.form['email'],
            "password": request.form['password']
        }
        response = auth_service.login(loginform)
        if not response['success']:
            flash(response['message'], 'error')
            return render_template('signin.html')
        return redirect('/dashboard')