import requests


class InternetService:
    """ Calls the USDA API for food information"""
    def __init__(self, app):
        self.key = app.config['USDA_KEY']

    def call_usda(self,food: str) -> list | None:
        """Returns a list of foods found based on the search criteria"""
        db = 'Foundation'
        food_list = []
        #call the USDA
        try:
            response = requests.get(
                #currently only call the foundation foods. V2 can use the SR database
                f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={self.key}&query={food}&dataType={db}&pagesize=50&page=1')

            # Everything beyond this is just formatting
            json = response.json()
            for food in json['foods']:
                foods_desc = {
                    'id': food['fdcId'],
                    'description': food['description'],
                }
                food_list.append(foods_desc)
            return food_list
        except Exception as e:
            #Food does not exist
            return None

    def get_specific_food(self, id):
        """Returns specific nutrient data based on the item chosen"""
        pass