
class FoodItem:
    def __init__(self, nutrients):
        self.nutrientvalues = {
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
            if key in self.nutrientvalues:
                self.nutrientvalues[key] = value