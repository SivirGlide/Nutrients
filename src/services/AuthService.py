# Handles authentication
# Valid session checking, correct signups and logins
from src.entities.UserOBJ import UserOBJ


class AuthService:
    """
    Handles Signup and Login transaction
    Handles session data validation
    """
    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository

    def signup(self, signupform):
        #outside files call this method and only this method
        #parse errors back through here
        is_valid, errors = self.__validateSignupform(signupform)
        if not is_valid:
            return False, errors
        print('form is valid attempting to contact database...')
        #once implimented, this section here will use other layers to contact database
        print(signupform)
        user = UserOBJ(signupform)
        return self.__attemptSignup(user)

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
        if not signupform.get("name"):
            error = 'Username is required'
            validationerrors.append(error)
            is_valid = False
        if not signupform.get("email"):
            error = 'Email is required'
            validationerrors.append(error)
            is_valid = False
        if not signupform.get("password"):
            error = 'Password is required'
            validationerrors.append(error)
            is_valid = False
        if not signupform.get("confirmPassword"):
            error = 'Password confirmation is required'
            validationerrors.append(error)
            is_valid = False

        #email is in correct format
        email = signupform.get("email")
        if email.find("@") == -1 or email.find(".") == -1:
            error = 'Email must be a valid email address'
            validationerrors.append(error)
            is_valid = False

        #password is atleast 6 characters long and contains a capital letter
        password = signupform.get("password")
        if len(password) < 6:
            error = 'Password must be at least 6 characters'
            validationerrors.append(error)
            is_valid = False
        #password and confirm password are the same
        if signupform.get("confirmPassword") != signupform.get("password"):
            error = 'Passwords do not match'
            validationerrors.append(error)
            is_valid = False

        return is_valid, validationerrors or None

    def __validateLoginform(self, loginform):
        validationerrors = []
        is_valid = True
        if not loginform.get("email") or not loginform.get("password"):
            error = 'Fill out the fields'
            validationerrors.append(error)
            is_valid = False
        email = loginform.get("email")
        if email.find("@") == -1 or email.find(".") == -1:
            error = 'Email must be a valid email address'
            validationerrors.append(error)
            is_valid = False
        return is_valid, validationerrors or None

    def __attemptSignup(self, user: UserOBJ):
        return self.user_repository.register_user(user)
