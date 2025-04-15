from src.entities.FoodOBJ import FoodItem


class FoodRepository:

    def __init__(self, database):
        self.database = database

    def find_by_name(self, name) -> list[FoodItem]:
        """ Return all the Foods that correspond with the input name """
        pass

    def find_by_id(self, food_id) -> FoodItem:
        """ Return a specific Food"""
        pass

    def create_food(self, food: FoodItem) -> tuple[bool, str]:
        """ Inserts food to the database"""
        #extract the json from food object
        food_data = food.nutrientvalues
        return self.database.create_food(food_data)

    def edit(self, nutrients: dict[str, str]) -> bool:
        """ edit a Foods values """
        pass

    def delete(self, food_id) -> FoodItem:
        """ Delete Food from the database """
        pass