from abc import ABC, abstractmethod

from src.entities.user_object import UserObject


class DatabaseUserInterface(ABC):
    @abstractmethod
    def register_user(self, user: UserObject):
        """ Register user """
        pass
    @abstractmethod
    def login_user(self, login_form: dict):
        """ Login user """
        pass
    @abstractmethod
    def get_user_uuid(self, user: UserObject):
        """ Get user uuid"""
        pass
    @abstractmethod
    def get_username(self, user: UserObject):
        """ Get username """
        pass
