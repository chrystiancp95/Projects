class Banco:
    """
    Classe para criar objetos 'Banco'.
    :return None
    """
    def __init__(self):
        self._agencias = [1111, 2222, 3333, 4444]
        self._contas = []
        self._clientes = []

    # todo Encontrar uma forma de fazer Type Hints das instancias.
    def autentificar(self, cliente: object):
        """
        Método para autentificar as operações da conta. Só é possível
        realizar saque/depósito se cliente, conta e agência estiverem salvos
        em banco.
        :param: cliente: object
        :return bool
        """
        print('Tentando Autentificar...')
        if cliente not in self._clientes:
            print('Falha: Cliente não cadastrado')
            return False
        if cliente.conta not in self._contas:
            print('Falha: Conta não cadastrada')
            return False
        if cliente.conta.agencia not in self._agencias:
            print('Falha: Agência não cadastrada')
            return False

        print('Autentificação bem sucedida.')
        return True

    def _inserir_contas(self, cliente: object):
        """
        Método para inserir contas no atributo self._contas. Método Local.
        :param: cliente: object
        :return None
        """
        self._contas.append(cliente.conta)

    def inserir_cliente(self, cliente):
        """
        Método para inserir clientes no atributo self._clientes e chamar
        _inserir_contas.
        :param cliente:
        :return:
        """
        if cliente not in self._clientes:
            self._clientes.append(cliente)
            self._inserir_contas(cliente)
