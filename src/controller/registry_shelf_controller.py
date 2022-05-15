from src.model.entities.shelf import Shelf
from src.model.shelf_repository import shelf_registry


class RegistryShelfController:
    def registry_shelf(self, shelf_number: int) -> any:
        try:
            self.__get_shelf_id(shelf_number)

            new_shelf = Shelf(
                id=shelf_number,
                number_of_shelf=shelf_number
            )
            shelf_registry.registry_shelf(new_shelf)
            
            return {"success": True, "shelf_registry": new_shelf}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __get_shelf_id(self, shelf_id: int) -> any:
        shelf_information = shelf_registry.get_shelf_id(shelf_id)
        if shelf_information != None: raise Exception(f'{shelf_id} prateleira já foi cadastrada.')
