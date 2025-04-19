from src.repositories.Meals import Meal_Repository


class MealService():
    def __init__(self, repository: Meal_Repository):
        self.repository = repository

    def get_meals(self, uuid: str) -> dict:
        """ Gets the meals of today based on the uuid, returns an empty json if no meals were found """
        return self.repository.get_meals(uuid)
