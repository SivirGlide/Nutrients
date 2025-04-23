""" Module for sending food information through the application."""

class FoodObject:
    """ To parse food information throughout the application."""
    def __init__(self):
        """ Create empty FoodObject"""
        self.nutrient_values = {}

    def get_nutrients(self) -> dict:
        """ Get nutrient information on the food object"""
        return self.nutrient_values

    def set_nutrients(self, nutrients: dict) -> None:
        """ Set nutrient information on the food object to the incoming dictionary"""
        self.nutrient_values = nutrients