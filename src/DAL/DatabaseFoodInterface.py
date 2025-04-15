from abc import ABC, abstractmethod

from src.Pages.data.domain.FoodOBJ import FoodItem


class DatabaseFoodInterface(ABC):
    @abstractmethod
    def create_food(self, food_values: dict[str,str]) -> tuple[bool, str]:
        pass

    @abstractmethod
    def read_food(self, food_attribute: str) -> dict[str, str]:
        """ Find a list of foods by given food_attribute """
        pass

    @abstractmethod
    def update_food(self, food: FoodItem) -> tuple[bool, str]:
        pass

    @abstractmethod
    def delete_food(self, food: FoodItem) -> tuple[bool, str]:
        pass
