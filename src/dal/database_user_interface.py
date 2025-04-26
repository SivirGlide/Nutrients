""" A module template for handling user data with a database """

from abc import ABC, abstractmethod
from src.entities.user_object import UserObject

class DatabaseUserInterface(ABC):
    """ Class format for Database user interfaces """
    @abstractmethod
    def register_user(self, user: UserObject):
        """ Register user """

    @abstractmethod
    def login_user(self, login_form: dict):
        """ Login user """

    @abstractmethod
    def get_user_uuid(self, user: UserObject):
        """ Get user uuid"""

    @abstractmethod
    def get_username(self, user: UserObject):
        """ Get username """
