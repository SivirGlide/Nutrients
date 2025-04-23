from src.DAL.DatabaseUserInterface import DatabaseUserInterface
from src.entities.user_object import UserObject


class UserRepository:
    def __init__(self, database: DatabaseUserInterface):
        self.database = database

    def register_user(self, user: UserObject) -> dict:
        return self.database.register_user(user)

    def login_user(self, login_form: dict) -> dict or str:
        return self.database.login_user(login_form)

    def get_user_uuid(self, user: UserObject) -> str or dict:
        #return the uuid as string or error
        return self.database.get_user_uuid(user)

    def get_username(self, user: UserObject):
        return self.database.get_username(user)