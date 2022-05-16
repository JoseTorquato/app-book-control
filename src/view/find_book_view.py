import os


class FindBookView:
    def find_book_view(self) -> str:
        self.__clear()
        print('\t Busca de prateleira \n ')
        try:
            find_shelf = int(input("\tQual o número da prateleira: "))
            return find_shelf
        except:
            print('\tO valor digitado não é um número.\n')
            return None

    def find_success(self, books: any) -> None:
        self.__clear()

        message = f'''
                * Livros encontrados na prateleira:  
            '''
        print(message)
        for book in books:
            format = self.__format_book_view(book)
            message = f'''
                * Livro:
                    Nome: {format["name"]}
                    Autor: {format["author"]}
            '''
            print(message)

    def find_fail(self, error) -> None:
        self.__clear()

        message = f'\tOcorreu ao procurar a prateleira: {error} '
        print(message)


    def __format_book_view(self, book):
        return {
            "id": book.id,
            "name": book.name,
            "author": book.author,
            "shelf": book.shelf_number
        }
    def __clear(self):
        os.system('cls||clear')
