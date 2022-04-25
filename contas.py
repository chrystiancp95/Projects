from abc import ABC, abstractmethod


class Conta(ABC):
    """
    Classe para criar objetos 'Conta'.
    :param agencia: int
    :param conta: str
    :param saldo: float
    :return None
    """
    def __init__(self, agencia: int, conta: str, saldo: float = 0.0) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: float):
        """Método para adicionar valores ao saldo.
        :param valor: float
        """
        self._saldo += valor

    def mostrar_dados(self):
        """Método para mostrar todos os dados relevantes da conta. """
        print(self.agencia, self.conta, self.saldo)

    @abstractmethod
    def sacar(self, valor):
        """Método abstrato para sacar do saldo. A subclasse deve polimorfar"""
        pass


class ContaCorrente(Conta):
    """
    Classe para criar objetos 'Conta Corrente'. Contas correntes podem ficar
    negativadas até o limite estabelecido.
    :param agencia: int
    :param conta: str
    :param saldo: float
    :param limite_negativo = 0.0
    :return None
    """
    def __init__(self, agencia: int, conta: str,
                 saldo: float = 0.0, limite_negativo: float = 0.0) -> None:
        super().__init__(agencia, conta, saldo)
        self._limite_negativo = limite_negativo

    def checar_valor_saque(self, valor: float) -> bool:
        """
        Checa se o valor do saque não é maior que a soma do saldo atual com
        o limite negativo.
        :param valor: float
        """
        saque_maximo = self._limite_negativo + self._saldo
        if valor > saque_maximo:
            print('Saldo insuficiente.')
            return False
        else:
            return True

    def sacar(self, valor: float) -> None:
        """ Subtrai o valor do saldo se checar_valor_saque for True
        :param valor: float
        """
        if self.checar_valor_saque(valor):
            self._saldo -= valor


class ContaPoupanca(Conta):
    """
    Classe para criar objetos 'Conta Corrente'. Contas correntes podem ficar
    negativadas até o limite estabelecido.
    :param agencia: int
    :param conta: str
    :param saldo: float
    :return None
    """
    def __init__(self, agencia: int, conta: str,
                 saldo: float = 0.0) -> None:
        super().__init__(agencia, conta, saldo)

    def checar_valor_saque(self, valor: float) -> bool:
        """
        Checa se o valor do saque não é maior que o saldo atual.
        :param valor: float
        """
        if valor > self.saldo:
            print('Saldo insuficiente.')
            return False
        else:
            return True

    def sacar(self, valor: float) -> None:
        """ Subtrai o valor do saldo se checar_valor_saque for True
        :param valor: float
        """
        if self.checar_valor_saque(valor):
            self._saldo -= valor


if __name__ == '__main__':
    print('Teste Conta')
    conta_teste = Conta(1111, '012345')
    conta_teste.depositar(1000.00)
    conta_teste.mostrar_dados()
    print('')

    print('Teste Conta Corrente')
    conta_corrente_teste = ContaCorrente(2222, '012345', 1000.00, 2000.00)
    conta_corrente_teste.depositar(1000.00)
    conta_corrente_teste.sacar(500.00)
    conta_corrente_teste.mostrar_dados()
    conta_corrente_teste.sacar(2000.00)
    conta_corrente_teste.mostrar_dados()
    conta_corrente_teste.sacar(2000.00)
    print('')

    print('Teste Conta Poupança')
    conta_poupanca_teste = ContaPoupanca(3333, '012345', 2000.00)
    conta_poupanca_teste.depositar(1000.00)
    conta_poupanca_teste.sacar(750.00)
    conta_poupanca_teste.sacar(1000.00)
    conta_poupanca_teste.mostrar_dados()
    conta_poupanca_teste.sacar(10000.00)
    print('')
