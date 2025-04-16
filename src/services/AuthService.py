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

    def signup(self, signupform) -> dict:
        #outside files call this method and only this method
        #parse errors back through here
        hashedsignupform, response = self.__validateSignupform(signupform)
        if not response["success"]:
            return response
        print(f'{response['error_code']} {response['message']}')

        #once implimented, this section here will use other layers to contact database
        user = UserOBJ(hashedsignupform)
        db_response = self.__attemptSignup(user)
        return db_response

    def login(self, loginform):
        is_valid, errors = self.__validateLoginform(loginform)
        if not is_valid:
            return False, errors
        print('form is valid attempting to log in...')
        return True, None

    def __validateSignupform(self, signupform) -> tuple:
        # ** turns json into outgoing format
        try:
            valid_form = ValidateSignupForm(**signupform)

            hashed_form = valid_form.model_dump()
            # hashed_form['password'] = generate_password_hash(
            #     hashed_form['password'],
            #     method='pbkdf2:sha256',
            #     salt_length=16
            # )
            # hashed_form.pop('confirm_password')
            response = {
                'success': True,
                'error_code': 200,
                'message': 'Form validated successfully!'
            }
            # due to supabase hashing itself we will ignore the hashing above and re implement another time
            hashed_form.pop('confirm_password')
            return hashed_form, response
        except ValueError as e:
            return signupform, {
                'success': False,
                'error_code': 400,
                'message': str(e)
            }
        except Exception as e:
            return signupform, {
                'success': False,
                'error_code': 500,
                'message': str(e)
            }

    def __validateLoginform(self, loginform):
        pass

    def __attemptSignup(self, user: UserOBJ) -> dict:
        return self.user_repository.register_user(user)