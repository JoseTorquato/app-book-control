from src.model.entities.shelf import Shelf


class RegistryShelfController:
    def registry_shelf(self, shelf_number: int) -> any:
        try:
            new_shelf = Shelf(
                id=shelf_number,
                number_of_shelf=shelf_number
            )
        
            return {"success": True, "shelf_registry": new_shelf}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
