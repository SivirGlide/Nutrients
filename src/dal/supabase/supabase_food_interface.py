""" A module for handling foods within supabase specifically """
import json
from datetime import datetime

from flask import session

from src.dal.database_food_interface import DatabaseFoodInterface
from src.entities.food_object import FoodObject


def extract_nutrient_value(nutrients_data, possible_keys):
    """
    Helper function to extract nutrient values, trying multiple possible key names.
    Returns the value without units, or "0" if not found.
    """
    for key in possible_keys:
        if key in nutrients_data:
            value = nutrients_data[key]
            if value:
                # Remove units (like 'g', 'mg', 'kcal', 'kJ') and return just the number
                import re
                # Extract just the numeric part
                numeric_value = re.findall(r'[\d.]+', str(value))
                return numeric_value[0] if numeric_value else "0"
    return "0"


class SupabaseFoodInterface(DatabaseFoodInterface):
    """ A class to handle supabase foods within supabase """
    def __init__(self, supabase):
        self.table_name = 'food'
        self.supabase = supabase

    def get_food_by_id(self, food_id: str):
        """ Find a list of foods by given food_attribute """
        response = (self.supabase
                    .table('food')
                    .select('*')
                    .eq('id', food_id).execute())
        if not response.data:
            print('No food found')
            return None
        response_data = json.loads(response.data[0]['Nutrients'])
        return response_data

    def create_food(self, food: FoodObject) -> None:
        """ Create a new food item """
        temp = {
            'id':food.get_nutrients()['id'],
            'Nutrients':food.get_nutrients()
        }
        self.supabase.table('food').insert(temp).execute()

    def update_food(self, food: FoodObject) -> tuple[bool, str]:
        """ Update food item """

    def delete_food(self, food: FoodObject) -> tuple[bool, str]:
        """ Delete a food item """

    def post_food(self, food: FoodObject):
        """ Post a food item to the Supabase eaten food table"""
        temp = {
            'food_id':food.get_nutrients()['id'],
            'user_id':session.get('uuid'),
        }
        self.supabase.table('eaten_food').insert(temp).execute()

    def get_eaten_foods_by_session(self, sessionid):
        date = datetime.today().strftime('%Y-%m-%d')
        response = (self.supabase
                    .table('eaten_food')
                    .select('*')
                    .eq('user_id', sessionid)
                    .eq('date_eaten', date)
                    .execute())
        food_id_list = []
        for item in response.data:
            food_id_list.append(item['food_id'])
        response = (self.supabase
                    .table('food')
                    .select('*')
                    .in_('id',food_id_list)
                    .execute())
        food_names = []
        for item in response.data:
            nutrients_dict = json.loads(item['Nutrients'])
            food_name = nutrients_dict['name']
            food_names.append(food_name)
        return food_names

    def get_eaten_food_ids_by_session(self):
        date = datetime.today().strftime('%Y-%m-%d')
        sessionuuid = session.get('uuid')

        response = (self.supabase
                    .table('eaten_food')
                    .select('*')
                    .eq('user_id', sessionuuid)
                    .eq('date_eaten', date)
                    .execute())

        food_id_list = []
        for item in response.data:
            food_id_list.append(item['food_id'])

        response = (self.supabase
                    .table('food')
                    .select('*')
                    .in_('id', food_id_list)
                    .execute())

        formatted_food_list = []

        for food_item in response.data:
            nutrients_data = json.loads(food_item['Nutrients'])
            food_name = nutrients_data.get('name', 'Unknown Food')

            required_nutrients = {
                "Calories": extract_nutrient_value(nutrients_data, ['Energy (Atwater General Factors)',
                                                                    'Energy (Atwater Specific Factors)', 'Energy']),
                "Fat": extract_nutrient_value(nutrients_data, ['Total lipid (fat)']),
                "Carbohydrates": extract_nutrient_value(nutrients_data, ['Carbohydrate, by difference']),
                "Sugar": extract_nutrient_value(nutrients_data, ['Sugars, Total']),
                "Protein": extract_nutrient_value(nutrients_data, ['Protein']),
                "Fibre": extract_nutrient_value(nutrients_data, ['Fiber, total dietary'])
            }

            formatted_item = {
                "Name": food_name,
                "Nutrients": required_nutrients
            }

            formatted_food_list.append(formatted_item)

        return formatted_food_list

