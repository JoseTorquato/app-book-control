import os


class RegistryBookView:
    def __init__(self) -> None:
        pass
    
    def registry_book_view(self):
        self.__clear()

        print("\tCadastrar um livro a uma prateleira \n\n")
        try:
            book_name = input("\tNome do livro:")
            author_name = input("\tAutor do livro:")
            shelf_id = int(input("\tQual o número da prateleira que o livro se encontra: "))
            
            return {
                "book": book_name,
                "author": author_name,
                "shelf": shelf_id
            }

        except:
            print('\tO valor digitado não é um número.\n')
            return None

    def registry_success_book(self, new_book: any) -> None:
        self.__clear()

        message = f'\tLivro {new_book.name} cadastrado com sucesso.'
        print(message)

    def registry_fail_book(self, new_book: any) -> None:
        self.__clear()

        message = f'\tOcorreu um erro ao cadastrar o livro: {new_book}.'
        print(message)

    def __clear(self):
        os.system('cls||clear')
