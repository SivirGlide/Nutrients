from src.entities.food_object import FoodObject
from src.repositories.Food import FoodRepository
from src.services.internal_internet_service import InternetService

#Handles validation of foods, creation of foods and directs database operations
class FoodService:
    def __init__(self, repository: FoodRepository, internet: InternetService):
        self.repository = repository
        self.internet = internet

    def create_food(self, food_json: dict[str,str]) -> tuple[bool, str]:
        """Create a new Food object and attempt to store it in the database. Takes a nutrients Json
        for an argument and returns boolean for outcome, with error code if error """
        food = FoodObject(food_json)
        return self.repository.create_food(food)

    def get_food_list(self, food_name: str) -> list | None:
        """Searches for the foods in USDA database,
         then attempts to contact supabase for the food details,
         if it doesn't exist go back to the usda"""
        return self.internet.call_usda(food_name)
        #self.repository.get_food()

    def get_food_from_list(self):
        pass
        # try:
        #     self.repository.get_food()
        # except Exception as e:
        #     self.internet.get_specific_food()
        #     self.repository.create_food()
        #     self.repository.get_food()
