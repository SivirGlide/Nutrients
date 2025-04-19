from src.entities.UserOBJ import UserOBJ
from src.repositories.User import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_name(self, form: dict):
        user = UserOBJ(form)
        return self.repository.get_username(user)
