from src.DAL.DatabaseFoodInterface import DatabaseFoodInterface
from src.entities.food_object import FoodObject
import json


class SupabaseFoodInterface(DatabaseFoodInterface):
    def __init__(self, supabase):
        self.table_name = 'food'
        self.supabase = supabase

    def get_food_by_id(self, food_id: str):
        """ Find a list of foods by given food_attribute """
        response = self.supabase.table('food').select('*').eq('id', food_id).execute()
        if not response.data:
            print('No food found')
            return None
        else:
            response_data = json.loads(response.data[0]['Nutrients'])
            return response_data

    def create_food(self, food: FoodObject) -> None:
        """ Create a new food item """
        print(food.get_nutrients())
        temp = {
            'id':food.get_nutrients()['id'],
            'Nutrients':food.get_nutrients()
        }
        self.supabase.table('food').insert(temp).execute()

    def update_food(self, food: FoodObject) -> tuple[bool, str]:
        pass

    def delete_food(self, food: FoodObject) -> tuple[bool, str]:
        """ Delete a food item """
        pass