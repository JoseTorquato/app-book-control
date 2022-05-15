class __ShelfRegister:
    def __init__(self) -> None:
        self.shelves = []
        self.books = []
    
    def registry_shelf(self, shelf_class: any) -> None:
        self.shelves.append(shelf_class)
    
    def get_shelf_id(self, shelf_id):
        for shelf_information in self.shelves:
            if shelf_information.id == shelf_id:
                return shelf_information
        
        return None


shelf_registry = __ShelfRegister()
