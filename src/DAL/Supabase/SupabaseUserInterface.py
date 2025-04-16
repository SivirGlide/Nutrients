from src.DAL.DatabaseUserInterface import DatabaseUserInterface
from src.entities.UserOBJ import UserOBJ


class SupabaseDatabaseUser(DatabaseUserInterface):
    def __init__(self, supabase):
        self.supabase = supabase

    def register_user(self, user: UserOBJ) -> dict:
        public_table_data = {
            'name':user.user['name'],
            'email':user.user['email']
        }
        auth_table_data = {
            'name': user.user['name'],
            'email': user.user['email'],
            'password': user.user['password']
        }
        # try supabase submission,
        try:
            self.supabase.auth.sign_up(auth_table_data)
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

    def get_user_session(self, username: str):
        pass
    def logout_user(self, user: UserOBJ):
        pass
    def get_user_uuid(self, username: str):
        pass
    def login_user(self, username: str):
        pass