from typing import Dict

from src.model.shelf_repository import shelf_registry


class FindBookController:
    def find(self, shelf_number: int) -> Dict:
        try:
            shelf_informations = self.__search_shelf(shelf_number)
            
            return {"success": True, "shelf_informations": shelf_informations}
        except Exception as exception:
            return {"success": False, "error": exception}

    def __search_shelf(self, shelf_number: int) -> any:
        shelf_informations = shelf_registry.get_books_by_shelf(shelf_number)
        if len(shelf_informations) == 0: raise Exception('Nesta prateleira não foi encontrado livros.')
        return shelf_informations
