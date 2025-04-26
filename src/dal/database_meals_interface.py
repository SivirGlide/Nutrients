""" A module template for handling meal data with a database """

from abc import ABC, abstractmethod

class DatabaseMealsInterface(ABC):
    """ Class format for Database meal interfaces """
    @abstractmethod
    def get_meals_by_user(self, uuid: str) -> list[dict]:
        """ Get meals by specific user """

    @abstractmethod
    def create_meal(self):
        """ Create meal """
