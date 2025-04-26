""" A module for handling users within supabase specifically """
from src.dal.database_user_interface import DatabaseUserInterface
from src.entities.user_object import UserObject


class SupabaseDatabaseUser(DatabaseUserInterface):
    """ A class to handle supabase users within supabase """
    def __init__(self, supabase):
        self.supabase = supabase

    def register_user(self, user: UserObject) -> dict:
        """ Try to sign the user up, return a dictionary including error code and message of outcome"""
        auth_table_data = {
            'email': user.user['email'],
            'password': user.user['password'],
            'options': {
                'data': {
                    'display_name': user.user['name'],
                }
            }
        }

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

    def get_user_uuid(self, user: UserObject) -> str or dict:
        """ return uuid of user based on user email """
        try:
            uuid = (self.supabase
                    .table('user')
                    .select('id')
                    .eq('email',user.user['email'])
                    .execute())
            uuid = uuid[0]['data']['id']
        except Exception as e:
            return {
                'success': False,
                'error_code': 500,
                'message': 'Error getting user_id: ' + str(e)
            }
        return uuid

    def login_user(self, login_form: dict) -> str or dict:
        """ Try to log the user in,
        return an uuid string if successful or and error dictionary if not"""
        try:
            result = (self.supabase
                      .auth
                      .sign_in_with_password(login_form))
            uuid = result.user.id
            return uuid
        except Exception as e:
            return {
                'success': False,
                'error_code': 499,
                'message': str(e)
            }

    def get_username(self, user: UserObject):
        """ return username of user based on user uuid"""
        try:
            result, error = (self.supabase
                             .table('user')
                             .select('name')
                             .eq('id', user.user['uuid'])
                             .execute())
            return result[1][0]['name']
        except Exception as e:
            return "Failed to get username: " + str(e)
