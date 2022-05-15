from src.controller.registry_shelf_controller import RegistryShelfController
from src.view.registry_shelf_view import RegistryShelfViews


def registry_shelf_process() -> any:
    registry_shelf_view = RegistryShelfViews()
    registry_shelf_controller = RegistryShelfController()

    shelf_number = registry_shelf_view.registry_shelf_view()
    response = registry_shelf_controller.registry_shelf(shelf_number)
    
    if response["success"]: registry_shelf_view.registry_success_shelf(response["shelf_registry"])
    else: registry_shelf_view.registry_fail_shelf(response["error"])
