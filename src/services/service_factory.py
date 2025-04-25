from src.dal.supabase.supabase_meals_interface import SupabaseMealsInterface
from src.dal.supabase.supabase_user_interface import SupabaseDatabaseUser
from src.dal.supabase.supabase_food_interface import SupabaseFoodInterface
from src.repositories.Food import FoodRepository
from src.repositories.Meals import Meal_Repository
from src.repositories.User import UserRepository
from src.services.food_service import FoodService
from src.services.auth_service import AuthService
from src.services.internal_internet_service import InternetService
from src.services.meal_service import MealService
from src.services.user_service import UserService


def init_services(app):
    #inject the supabase interface into the repository and the food repository into the food service
    supabase_food_interface = SupabaseFoodInterface(app.supabase)
    food_repository = FoodRepository(supabase_food_interface)

    supabase_meal_interface = SupabaseMealsInterface(app.supabase)
    meal_repository = Meal_Repository(supabase_meal_interface)

    supabase_auth = SupabaseDatabaseUser(app.supabase)
    auth_repository = UserRepository(supabase_auth)

    user_repository = UserRepository(supabase_auth)

    internet_service = InternetService(app)


    auth_service = AuthService(auth_repository)
    food_service = FoodService(food_repository, internet_service)
    meal_service = MealService(meal_repository)
    user_service = UserService(user_repository)
    return {
        'auth_service': auth_service,
        'food_service': food_service,
        'meal_service': meal_service,
        'user_service': user_service
    }