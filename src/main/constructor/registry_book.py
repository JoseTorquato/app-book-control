from src.controller.registry_book_controller import RegistryBookController
from src.view.registry_book_view import RegistryBookView


def registry_book_process() -> None:
    registry_book_view = RegistryBookView()
    registry_book_controller = RegistryBookController()

    book_informations = registry_book_view.registry_book_view()
    response = registry_book_controller.registry_book(book_informations)

    if response["success"]: registry_book_view.registry_success_book(response["book_registry"])
    else: registry_book_view.registry_fail_book(response["error"])
