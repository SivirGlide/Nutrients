from src.entities.FoodOBJ import FoodItem
from src.repositories.Food import FoodRepository


#Handles validation of foods, creation of foods and directs database operations
class FoodService:
    def __init__(self, repository: FoodRepository):
        self.repository = repository

    def create_food(self, food_item: dict[str,str]) -> tuple[bool, str]:
        """Create a new Food object and attempt to store it in the database. Takes a nutrients Json
        for an argument and returns boolean for outcome, with error code if error """
        food = FoodItem(food_item)
        return self.repository.create_food(food)

