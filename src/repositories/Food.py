from src.entities.food_object import FoodObject


class FoodRepository:

    def __init__(self, database):
        self.database = database

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

    def get_eaten_foods_by_session(self, session_id):
        """ Return a list of Foods """
        return self.database.get_eaten_foods_by_session(session_id)

    def get_eaten_food_ids_by_session(self):
        """ Return a list of Food ids """
        return self.database.get_eaten_food_ids_by_session()
