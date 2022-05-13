import os


class RegistryShelfViews:
    def registry_sheld_view(self) -> int:
        self.__clear()
        print("\tCadastrar uma prateleira \n\n")
        try:
            shelf_number = int(input("\tQual o número da prateleira: "))
            return shelf_number
        except:
            print('\tO valor digitado não é um número.\n')
            return None

    def registry_success_shelf(self, new_shelf: any) -> None:
        self.__clear()

        message = f'\tPrateleira número {new_shelf.id} cadastrada com sucesso'
        print(message)

    def registry_fail_shelf(self, new_shelf: any) -> None:
        self.__clear()

        message = f'\tOcorreu um erro ao cadastrar a prateleira: {new_shelf.id}'
        print(message)
        
    def __clear(self) -> None:
        os.system('cls||clear')
