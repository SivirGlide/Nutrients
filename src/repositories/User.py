from src.DAL.DatabaseUserInterface import DatabaseUserInterface
from src.entities.UserOBJ import UserOBJ


class UserRepository:
    def __init__(self, database: DatabaseUserInterface):
        self.database = database

    def register_user(self, user: UserOBJ) -> dict:
        return self.database.register_user(user)

    def login_user(self, login_form: dict) -> dict or None:
        return self.database.login_user(login_form)

    def get_user_uuid(self, user: UserOBJ) -> str or dict:
        #return the uuid as string or error
        return self.database.get_user_uuid(user)