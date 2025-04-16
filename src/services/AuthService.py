# Handles authentication
# Valid session checking, correct signups and logins
from werkzeug.security import generate_password_hash

from src.entities.UserOBJ import UserOBJ
from src.services.auth_services.FormValidationAuthHelper import ValidateSignupForm


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
        # ** turns json into outgoing format
        try:
            validate_form = ValidateSignupForm(**signupform)
            hashed_form = validate_form.model_dump()
            hashed_form['password'] = generate_password_hash(
                hashed_form['password'],
                method='pbkdf2:sha256',
                salt_length=16
            )
            hashed_form.pop('confirm_password')
            return hashed_form
        except ValueError as e:
            return {
                'success': False,
                'error_code': 400,
                'message': str(e)
            }
        except Exception as e:
            return {
                'success': False,
                'error_code': 500,
                'message': str(e)
            }

    def __validateLoginform(self, loginform):
        pass

    def __attemptSignup(self, user: UserOBJ):
        return self.user_repository.register_user(user)