from src.DAL.DatabaseFoodInterface import DatabaseFoodInterface
from src.Pages.data.domain.FoodOBJ import FoodItem


class SupabaseInterface(DatabaseFoodInterface):
    def __init__(self, client):
        self.table_name = 'food'
        self.client = client

    def read_food(self, food_attribute: str) -> dict[str, str]:
        """ Find a list of foods by given food_attribute """
        pass

    def create_food(self, food_values: dict[str,str]) -> tuple[bool, str]:
        """ Create a new food item """
        return True, 'You Hit the Supabase Layer'

    def update_food(self, food: FoodItem) -> tuple[bool, str]:
        pass

    def delete_food(self, food: FoodItem) -> tuple[bool, str]:
        """ Delete a food item """
        pass