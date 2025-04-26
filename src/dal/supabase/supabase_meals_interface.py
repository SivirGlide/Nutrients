""" A module for handling meals within supabase specifically """

from datetime import datetime
from src.dal.database_meals_interface import DatabaseMealsInterface

class SupabaseMealsInterface(DatabaseMealsInterface):
    """ A class to handle supabase meals within supabase """
    def __init__(self, supabase):
        self.supabase = supabase

    def get_meals_by_user(self, uuid: str) -> list[dict] | None:
        """ get a meal based on uuid, returns dictionary response or None"""
        try:

            date = datetime.today().strftime('%Y-%m-%d')
            response, error = (
                self.supabase.table("eaten_meals")
                .select("*").eq('uuid', uuid)
                .eq('date_time', date)
                .execute())
            meal_list = []
            for item in response[1]:
                meal_list.append(item['meal_id'])
            print(meal_list)
            get_meal_name, error = (
                self.supabase
                .table("meals")
                .select("name")
                .in_('id', meal_list)
                .execute())
            return get_meal_name[1]
        except Exception as e:
            print(e)
            return None

    def create_meal(self):
        """ Create meal in the supabase db: return error code as response"""
