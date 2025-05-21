from src.entities.food_object import FoodObject


class FoodRepository:

    def __init__(self, database):
        self.database = database

    def find_by_name(self, name) -> list[FoodObject]:
        """ Return all the Foods that correspond with the input name """
        pass

    def find_by_id(self, food_id):
        """ Return a specific Food"""
        return self.database.get_food_by_id(food_id)

    def create_food(self, food: FoodObject) -> tuple[bool, str]:
        """ Inserts food to the database"""
        #extract the json from food object
        return self.database.create_food(food)

    def edit(self, nutrients: dict[str, str]) -> bool:
        """ edit a Foods values """
        pass

    def delete(self, food_id) -> FoodObject:
        """ Delete Food from the database """
        pass

    def post_food(self, food: FoodObject):
        """ Post a food object to the eaten food table"""
        return self.database.post_food(food)