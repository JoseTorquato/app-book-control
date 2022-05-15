from .constructor.registry_book import registry_book_process
from .constructor.registry_shelf import registry_shelf_process
from .constructor.start_process import start_process

command_mapping = {
    '1': registry_shelf_process,
    '2': registry_book_process
}

def start() -> None:
    while True:
        command = start_process()

        command_mapping[command]()
