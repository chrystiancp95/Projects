class Pessoa:
    """
    Classe para criar objetos 'Pessoas'
    :param nome: str
    :param sobrenome: str
    :param idade: int
    :param sexo: str
    :return: None
    """
    def __init__(self, nome: str, sobrenome: str, idade: int,
                 sexo: str) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._sexo = sexo

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def idade(self):
        return self._idade

    @property
    def sexo(self):
        return self._sexo

    def mostrar_dados(self) -> None:
        """ Método para mostrar todos os dados da instância de Pessoa. """
        print(self.nome, self.sobrenome, self.idade, self.sexo)


class Cliente(Pessoa):
    """
    Classe para criar objetos "Clientes" que herdam de "Pessoas".
    :param nome: str
    :param sobrenome: str
    :param idade: int
    :param sexo: str
    :return: None
    """
    def __init__(self, nome: str, sobrenome: str, idade: int,
                 sexo: str) -> None:
        """
        Construtor de Cliente: Inicia a supraclasse Pessoa e o atributo
        self._conta.
        """
        super().__init__(nome, sobrenome, idade, sexo)
        self._conta = None

    @property
    def conta(self):
        return self._conta

    def inserir_conta(self, conta) -> None:
        """Adiciona uma instância de "Conta" para o atributo self._conta do
        Cliente. """
        self._conta = conta

    def mostrar_dados(self):
        """Método para mostrar todos os dados da conta de Cliente. """
        print(self.conta)


if __name__ == '__main__':
    teste_cliente = Cliente('Chrystian', 'Costa', 26, 'Masculino')
    teste_cliente.mostrar_dados()
    teste_cliente.inserir_conta('012345')
    teste_cliente.mostrar_dados()
