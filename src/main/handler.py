from .constructor.start_process import start_process
from .constructor.registry_shelf import registry_shelf_process

command_mapping = {
    '1': registry_shelf_process
}

def start() -> None:
    while True:
        command = start_process()

        command_mapping[command]()
