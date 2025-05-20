from src.dal.database_meals_interface import DatabaseMealsInterface


class Meal_Repository():
    def __init__(self, db: DatabaseMealsInterface):
        #Database goes here
        self.db = db

    def get_meals(self, uuid: str) -> list[dict]:
        return self.db.get_meals_by_user(uuid)