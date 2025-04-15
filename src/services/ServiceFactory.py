from src.repositories.Food import FoodRepository
from src.services.FoodService.FoodService import FoodService
from src.services.auth_services.AuthService import AuthService

food_repository = FoodRepository()

auth_service = AuthService()
food_service = FoodService(food_repository)