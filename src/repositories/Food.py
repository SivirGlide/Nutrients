from src.entities.food_object import FoodObject


class FoodRepository:

    def __init__(self, database):
        self.database = database

    def find_by_name(self, name) -> list[FoodObject]:
        """ Return all the Foods that correspond with the input name """
        pass

    def find_by_id(self, food_id) -> FoodObject:
        """ Return a specific Food"""
        pass

    def create_food(self, food: FoodObject) -> tuple[bool, str]:
        """ Inserts food to the database"""
        #extract the json from food object
        food_data = food.nutrient_values
        return self.database.create_food(food_data)

    def edit(self, nutrients: dict[str, str]) -> bool:
        """ edit a Foods values """
        pass

    def delete(self, food_id) -> FoodObject:
        """ Delete Food from the database """
        pass