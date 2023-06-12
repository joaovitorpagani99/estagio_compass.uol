class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None

    def set_nome(self, nome):
        self.__nome = nome

    def nome(self):
        return self.__nome

pessoa = Pessoa(0)
pessoa.set_nome('Fulano De Tal')
print(pessoa.nome())