from src.DAL.Supabase.SupabaseUserInterface import SupabaseDatabaseUser
from src.DAL.Supabase.SupabaseFoodInterface import SupabaseFoodInterface
from src.repositories.Food import FoodRepository
from src.repositories.User import UserRepository
from src.services.FoodService import FoodService
from src.services.AuthService import AuthService


def init_services(app):
    #inject the supabase interface into the repository and the food repository into the food service
    supabase_food_interface = SupabaseFoodInterface(app.supabase)
    food_repository = FoodRepository(supabase_food_interface)

    supabase_auth = SupabaseDatabaseUser(app.supabase)
    auth_repository = UserRepository(supabase_auth)

    auth_service = AuthService(auth_repository)
    food_service = FoodService(food_repository)
    return {
        'auth_service': auth_service,
        'food_service': food_service,
    }