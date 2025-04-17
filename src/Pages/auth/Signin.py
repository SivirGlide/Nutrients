from flask import render_template, request, flash


def getSignIn(auth_service):
    if request.method == 'GET':
        return render_template('signin.html')
    if request.method == 'POST':
        loginform = {
            "email": request.form['email'],
            "password": request.form['password']
        }
        auth_service.login(loginform)
        #
        # if not is_valid:
            # for error in errors:
            #     flash(error)
            #     return render_template('signin.html')
        return render_template('signin.html')


