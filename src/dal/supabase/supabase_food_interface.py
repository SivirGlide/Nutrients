""" A module for handling foods within supabase specifically """
import json

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