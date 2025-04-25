from abc import ABC, abstractmethod

from src.entities.food_object import FoodObject


class DatabaseFoodInterface(ABC):
    @abstractmethod
    def create_food(self, food_values: dict[str,str]) -> tuple[bool, str]:
        pass

    @abstractmethod
    def get_food_by_id(self, food_id: str) -> dict[str, str]:
        """ Find a food by id """
        pass

    @abstractmethod
    def update_food(self, food: FoodObject) -> tuple[bool, str]:
        pass

    @abstractmethod
    def delete_food(self, food: FoodObject) -> tuple[bool, str]:
        pass
