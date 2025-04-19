from datetime import datetime

from src.DAL.DatabaseMealsInterface import DatabaseMealsInterface


class SupabaseMealsInterface(DatabaseMealsInterface):
    def __init__(self, supabase):
        self.supabase = supabase

    def get_meals(self, uuid: str) -> list[dict]:
        try:

            date = datetime.today().strftime('%Y-%m-%d')
            response, error = self.supabase.table("eaten_meals").select("*").eq('uuid', uuid).eq('date_time', date).execute()
            meal_list = []
            for item in response[1]:
                meal_list.append(item['meal_id'])
            print(meal_list)
            get_meal_name, error = self.supabase.table("meals").select("name").in_('id', meal_list).execute()
            return get_meal_name[1]
        except Exception as e:
            print(e)
            return None