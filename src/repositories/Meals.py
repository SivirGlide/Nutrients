from src.DAL.DatabaseMealsInterface import DatabaseMealsInterface


class Meal_Repository():
    def __init__(self, db: DatabaseMealsInterface):
        #Database goes here
        self.db = db

    def get_meals(self, uuid: str) -> dict:
        return self.db.get_meals(uuid)