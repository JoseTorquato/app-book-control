from typing import Dict

from src.model.entities.book import Book
from src.model.shelf_repository import shelf_registry


class RegistryBookController:
    def registry_book(self, book_informations: Dict) -> any:
        try:
            self.__get_book_id(book_informations["book"])

            shelf_id = shelf_registry.get_shelf_id(book_informations["shelf"])
            if shelf_id == None: raise Exception(f"\n\n\tPrateleira {book_informations['shelf']} não encontrada.")

            new_book = Book(
                id=self.__new_books_id(),
                name=book_informations["book"],
                author=book_informations["author"],
                shelf_number=book_informations["shelf"]
            )


            shelf_registry.registry_book(new_book)

            return {"success": True, "book_registry": new_book}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __get_book_id(self, book_name: str) -> any:
        book_information = shelf_registry.get_book_name(book_name)
        if book_information != None: raise Exception(f'{book_name} já foi cadastrada na prateleira: {book_information.shelf}.')

    def __new_books_id(self):
        books = shelf_registry.get_all_books()
        return len(books) + 1
