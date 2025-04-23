from src.entities.user_object import UserObject
from src.repositories.User import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_name(self, form: dict):
        user = UserObject(form)
        return self.repository.get_username(user)
