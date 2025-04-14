# Handles authentication
# Valid session checking, correct signups and logins


class AuthService:
    """
    Validates the signup form data
    Returns (is_valid, error_message)
    """
    @staticmethod
    def validateSignup(signupform):
        validationerrors = []
        #all boxes are not empty
        if not signupform.get("Name"):
            error = 'Username is required'
            validationerrors.append(error)
            return False, validationerrors
        if not signupform.get("Email"):
            error = 'Email is required'
            validationerrors.append(error)
            return False, validationerrors
        if not signupform.get("Password"):
            error = 'Password is required'
            validationerrors.append(error)
            return False, validationerrors
        if not signupform.get("ConfirmPassword"):
            error = 'Password confirmation is required'
            validationerrors.append(error)
            return False, validationerrors
        #email is in correct format
        #run a check to see if email already exists in db
        #password is atleast 6 characters long and contains a capital letter
        #password and confirm password are the same
        print('form is valid sending you to the dashboard!')
        return True, None
