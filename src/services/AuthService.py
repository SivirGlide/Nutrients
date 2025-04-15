# Handles authentication
# Valid session checking, correct signups and logins


class AuthService:
    """
    Validates the signup form data
    Returns (is_valid, error_message)
    """
    def __init__(self):
        pass


    def signup(self, signupform):
        #outside files call this method and only this method
        #parse errors back through here
        is_valid, errors = self.__validateSignupform(signupform)
        if not is_valid:
            return False, errors
        print('form is valid attempting to contact database...')
        #once implimented, this section here will use other layers to contact database
        return True, None

    def login(self, loginform):
        is_valid, errors = self.__validateLoginform(loginform)
        if not is_valid:
            return False, errors
        print('form is valid attempting to log in...')
        return True, None

    def __validateSignupform(self, signupform):
        validationerrors = []
        is_valid = True
        #all boxes are not empty
        if not signupform.get("Name"):
            error = 'Username is required'
            validationerrors.append(error)
            is_valid = False
        if not signupform.get("Email"):
            error = 'Email is required'
            validationerrors.append(error)
            is_valid = False
        if not signupform.get("Password"):
            error = 'Password is required'
            validationerrors.append(error)
            is_valid = False
        if not signupform.get("ConfirmPassword"):
            error = 'Password confirmation is required'
            validationerrors.append(error)
            is_valid = False

        #email is in correct format
        email = signupform.get("Email")
        if email.find("@") == -1 or email.find(".") == -1:
            error = 'Email must be a valid email address'
            validationerrors.append(error)
            is_valid = False

        #password is atleast 6 characters long and contains a capital letter
        password = signupform.get("Password")
        if len(password) < 6:
            error = 'Password must be at least 6 characters'
            validationerrors.append(error)
            is_valid = False
        #password and confirm password are the same
        if signupform.get("ConfirmPassword") != signupform.get("Password"):
            error = 'Passwords do not match'
            validationerrors.append(error)
            is_valid = False

        return is_valid, validationerrors or None

    def __validateLoginform(self, loginform):
        validationerrors = []
        is_valid = True
        if not loginform.get("Email") or not loginform.get("Password"):
            error = 'Fill out the fields'
            validationerrors.append(error)
            is_valid = False
        email = loginform.get("Email")
        if email.find("@") == -1 or email.find(".") == -1:
            error = 'Email must be a valid email address'
            validationerrors.append(error)
            is_valid = False
        return is_valid, validationerrors or None
