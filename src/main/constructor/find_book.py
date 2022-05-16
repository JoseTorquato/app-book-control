from src.controller.find_book_controller import FindBookController
from src.view.find_book_view import FindBookView


def find_books_process() -> None:
    find_shelf_view = FindBookView()
    find_shelf_controller = FindBookController()

    shelf_id = find_shelf_view.find_book_view()
    response = find_shelf_controller.find(shelf_id)
    
    if response["success"]: find_shelf_view.find_success(response["shelf_informations"])
    else: find_shelf_view.find_fail(response["error"])
