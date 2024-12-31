class Process:
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str):
            print('Acessando o banco de dados...')
            print('Verificando existência do usuário...')
            print('Cadastro de usuário realizado com sucesso!')
        else:
            raise Exception('Dados Inválidos')