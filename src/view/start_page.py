def start_page() -> str:
    message = '''
        Sistema de cadastro

        * Cadastrar uma prateleira - 1
        * Cadastrar um livro - 2
        * Buscar livros em uma prateleira - 3
        * Sair - 0

    '''
    print(message)

    command = input('\tEscolha uma opção: ')

    return command
