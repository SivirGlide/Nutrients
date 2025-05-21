""" A module template for handling food data with a database """

from abc import ABC, abstractmethod
from src.entities.food_object import FoodObject

class DatabaseFoodInterface(ABC):
    """ Class template for handling food data with a database """

    @abstractmethod
    def create_food(self, food_values: dict[str,str]):
        """ Create a food entity """

    @abstractmethod
    def get_food_by_id(self, food_id: str):
        """ get a food entity by id """

    @abstractmethod
    def update_food(self, food: FoodObject):
        """ Update a food entity, currently has no use"""

    @abstractmethod
    def delete_food(self, food: FoodObject):
        """ Delete a food entity, currently has no use """

    @abstractmethod
    def post_food(self, food: FoodObject):
        """ Post a food entity to the eaten food table"""

    @abstractmethod
    def get_eaten_foods_by_session(self, session_id):
        """ Return a list of Foods """
