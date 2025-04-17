from src.DAL.DatabaseUserInterface import DatabaseUserInterface
from src.entities.UserOBJ import UserOBJ


class SupabaseDatabaseUser(DatabaseUserInterface):
    def __init__(self, supabase):
        self.supabase = supabase

    def register_user(self, user: UserOBJ) -> dict:
        auth_table_data = {
            'email': user.user['email'],
            'password': user.user['password'],
            'options': {
                'data': {
                    'display_name': user.user['name'],
                }
            }
        }
        # try supabase submission,
        try:
            result = self.supabase.auth.sign_up(auth_table_data)
            public_table_data = {
                'id': result.user.id,
                'name': user.user['name'],
                'email': user.user['email'],
            }
            self.supabase.table('user').insert(public_table_data).execute()
        except Exception as e:
            return {
                'success': False,
                'error_code':500,
                'message': str(e)
            }
        return {
            'success': True,
            'error_code': 200,
            'message': 'User registered successfully!'
        }

    def logout_user(self, user: UserOBJ):
        pass
    def get_user_uuid(self, user: UserOBJ) -> str or dict:
        try:
            uuid = self.supabase.table('user').select('id').eq('email',user.user['email']).execute()
            uuid = uuid[0]['data']['id']
        except Exception as e:
            return {
                'success': False,
                'error_code': 500,
                'message': 'Error getting user_id: ' + str(e)
            }
        return uuid

    def login_user(self, login_form: dict) -> str or dict:
        try:
            result = self.supabase.auth.sign_in_with_password(login_form)
            uuid = result.user.id
            return uuid
        except Exception as e:
            # Realistically this should check the error and return different codes,
            # but if my website isn't being exploited it will only return invalid details errors
            return {
                'success': False,
                'error_code': 499,
                'message': str(e)
            }