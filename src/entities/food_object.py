""" Module for sending food information through the application."""

class FoodObject:
    """ To parse food information throughout the application."""
    def __init__(self):
        """ Create empty FoodObject"""
        self.nutrient_values = {}

    def get_nutrients(self):
        """ Get nutrient information on the food object"""
        return self.nutrient_values

    def set_nutrients(self, nutrients):
        """ Set nutrient information on the food object"""
        for key, value in nutrients.items():
            self.nutrient_values[key] = value