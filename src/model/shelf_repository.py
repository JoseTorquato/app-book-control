from typing import List


class __ShelfRegister:
    def __init__(self) -> None:
        self.shelves = []
        self.books = []
    
    def registry_shelf(self, shelf_class: any) -> None:
        self.shelves.append(shelf_class)
    
    def registry_book(self, book_class: any) -> None:
        self.shelves.append(book_class)
    
    def get_shelf_id(self, shelf_id: int) -> any:
        for shelf_information in self.shelves:
            if shelf_information.id == shelf_id:
                return shelf_information
        
        return None
    
    def get_book_name(self, book_name: str) -> any:
        for book_information in self.books:
            if book_information.id == book_name:
                return book_information
        
        return None
    
    def get_all_books(self) -> List:
        return self.books

shelf_registry = __ShelfRegister()
