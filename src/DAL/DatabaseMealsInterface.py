from abc import ABC, abstractmethod


class DatabaseMealsInterface(ABC):

    @abstractmethod
    def get_meals(self, uuid: str) -> list[dict]:
        pass