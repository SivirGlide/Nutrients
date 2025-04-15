from abc import ABC, abstractmethod

from src.entities.UserOBJ import UserOBJ


class DatabaseUserInterface(ABC):
    @abstractmethod
    def register_user(self, user: UserOBJ):
        """ Register user """
        pass
    @abstractmethod
    def login_user(self, user: UserOBJ):
        """ Login user """
        pass
    @abstractmethod
    def logout_user(self, user: UserOBJ):
        """ Logout user """
        pass
    @abstractmethod
    def get_user_session(self, username: str):
        """ Get user session """
        pass
    @abstractmethod
    def get_user_uuid(self, username: str):
        """ Get user uuid"""
        pass
