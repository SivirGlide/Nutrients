from flask import current_app
from src.DAL.Supabase import SupabaseInterface
from src.repositories.Food import FoodRepository
from src.services.FoodService.FoodService import FoodService
from src.services.auth_services.AuthService import AuthService


def init_services(app):
    supabase_interface = SupabaseInterface(app.supabase)
    food_repository = FoodRepository(supabase_interface)

    auth_service = AuthService()
    food_service = FoodService(food_repository)
    return {
        'auth_service': auth_service,
        'food_service': food_service,
    }