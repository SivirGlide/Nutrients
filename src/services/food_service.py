from src.entities.food_object import FoodObject
from src.repositories.Food import FoodRepository
from src.services.internal_internet_service import InternetService

#Handles validation of foods, creation of foods and directs database operations
class FoodService:
    def __init__(self, repository: FoodRepository, internet: InternetService):
        self.repository = repository
        self.internet = internet
        self.food_object = FoodObject()

    def create_food(self, food_json: dict[str,str]) -> tuple[bool, str]:
        """Create a new Food object and attempt to store it in the database. Takes a nutrients Json
        for an argument and returns boolean for outcome, with error code if error """
        self.food_object.set_nutrients(food_json)
        return self.repository.create_food(self.food_object)

    def get_food_list(self, food_name: str) -> list | None:
        """Searches for the foods in USDA database"""
        return self.internet.call_usda(food_name)

    def get_food_by_id(self, food_id):
        """ Gets a food by id"""
        #Try to get the id from the database

        response = self.repository.find_by_id(food_id)
        if response is not None:
            self.food_object.set_nutrients(response)
            print(self.food_object.get_nutrients())
            return self.food_object
        food_dict = self.internet.get_food_by_id(food_id)
        if food_dict is None:
            return None
        self.food_object.set_nutrients(food_dict)
        #     # print(self.food_object.get_nutrients())
        #     # #Store the food object in the database by calling create_food
        self.repository.create_food(self.food_object)
        print(self.food_object.get_nutrients())
        return self.food_object

