""" A module for handling foods within supabase specifically """
import json
from datetime import datetime

from flask import session

from src.dal.database_food_interface import DatabaseFoodInterface
from src.entities.food_object import FoodObject

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
        #print(response.data)
        for item in response.data:
            nutrients_dict = json.loads(item['Nutrients'])

            # Now you can access the 'name' key from the dictionary
            food_name = nutrients_dict['name']
            food_names.append(food_name)
        return food_names