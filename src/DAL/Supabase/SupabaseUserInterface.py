from src.DAL.DatabaseUserInterface import DatabaseUserInterface
from src.entities.UserOBJ import UserOBJ


class SupabaseDatabaseUser(DatabaseUserInterface):
    def __init__(self, supabase):
        self.supabase = supabase

    def register_user(self, user: UserOBJ) -> tuple[bool, str]:
        public_table_data = {
            'name':user.user['name'],
            'email':user.user['email']
        }
        result = self.supabase.table('user').insert(public_table_data).execute()
        print(result)
        return True, "200"

    def get_user_session(self, username: str):
        pass
    def logout_user(self, user: UserOBJ):
        pass
    def get_user_uuid(self, username: str):
        pass
    def login_user(self, username: str):
        pass