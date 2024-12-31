""" 
S - Principio da Responsabilidade Única (SRP)

"Um módulo deve ter um, e apenas um, motivo para alteração"

Ele deve ser especializado em um único assunto e possuir apenas uma única responsabilidade dentro do seu software.

"Um módulo é apenas um conjunto coeso de funções e estruturas de dados"
"""

class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error('Dados Inválidos')
        
    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str, password: str) -> None:
        print('Acessando o banco de dados...')
        print('Verificando existência do usuário...')
    
    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuário realizado com sucesso!')
    
    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)
