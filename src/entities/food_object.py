""" Module for sending food information through the application."""

class FoodObject:
    """ To parse food information throughout the application.
    To be Refactored for use eventually,"""
    def __init__(self, nutrients):
        """ Pylist Test?"""
        self.nutrient_values = {
            "id":"",
            "Name":"",
            "Energy":"",
            "Fat":"",
            "Carbohydrates":"",
            "Sugars":"",
            "Protein":"",
            "Fibre":"",
            "Salt":""
        }
        #appends nutrientvalues with the incoming JSON
        for key, value in nutrients.items():
            if key in self.nutrient_values:
                self.nutrient_values[key] = value

    def get_nutrients(self):
        return self.nutrient_values

    def set_nutrients(self, nutrients):
        self.nutrient_values = nutrients