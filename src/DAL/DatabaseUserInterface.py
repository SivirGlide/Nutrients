from abc import ABC, abstractmethod

from src.entities.UserOBJ import UserOBJ


class DatabaseUserInterface(ABC):
    @abstractmethod
    def register_user(self, user: UserOBJ):
        """ Register user """
        pass
    @abstractmethod
    def login_user(self, login_form: dict):
        """ Login user """
        pass
    @abstractmethod
    def logout_user(self, user: UserOBJ):
        """ Logout user """
        pass
    @abstractmethod
    def get_user_uuid(self, user: UserOBJ):
        """ Get user uuid"""
        pass
