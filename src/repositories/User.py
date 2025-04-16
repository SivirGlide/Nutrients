from src.DAL.DatabaseUserInterface import DatabaseUserInterface
from src.entities.UserOBJ import UserOBJ


class UserRepository:
    def __init__(self, database: DatabaseUserInterface):
        self.database = database

    def register_user(self, user: UserOBJ) -> dict:
        return self.database.register_user(user)

    def login_user(self, user: UserOBJ) -> dict:
        pass