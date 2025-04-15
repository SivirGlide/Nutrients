from src.Pages.data.domain.FoodOBJ import FoodItem


class FoodRepository:

    def __init__(self):
        pass

    def find_by_name(self, name) -> list[FoodItem]:
        """ Return all the Foods that correspond with the input name """
        pass

    def find_by_id(self, food_id) -> FoodItem:
        """ Return a specific Food"""
        pass

    def save(self, food: FoodItem) -> tuple[bool, str]:
        """ Inserts food to the database"""
        #write attempt to save food
        return True, '200'

    def edit(self, nutrients: dict[str, str]) -> bool:
        """ edit a Foods values """
        pass

    def delete(self, food_id) -> FoodItem:
        """ Delete Food from the database """
        pass