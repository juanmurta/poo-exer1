from datetime import datetime
import pytz


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerencia as contas dos clientes.

    Atributos:
    nome (str): Nome do cliente
    cpf (str): CPF do cliente. Deve ser inserido com pontos e traços
    agencia (str): Número da agência
    num_conta (str): Número da conta
    saldo (int): Saldo da conta
    limite (int): Limite da conta
    transacoes (list): Lista de transações realizadas na conta

    """

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    def consultar_saldo(self):
        """
            Exibe o saldo atual da conta do cliente.
            Não possui parâmetros.
        """
        print(f'{self._nome} Seu saldo atual é de R$ {self._saldo:.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Saldo insuficiente')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite(self):
        print(f'Seu limite atual é de R$ {self._limite_conta():.2f}')

    def consultar_historico_transacoes(self):
        print('Histórico de transações')
        print('Valor, Saldo, Data/Hora')
        for transacoes in self._transacoes:
            print(transacoes)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))


# programa
conta_Juan = ContaCorrente('Juan', '123.456.789-00', '1234', '123456-7')
conta_Juan.consultar_saldo()

# depositando dinheiro na conta
conta_Juan.depositar(20000)

# sacando dinheiro da conta
conta_Juan.sacar_dinheiro(10500)

print('-' * 50)
conta_Ariany = ContaCorrente('Ariany', '987.654.321-00', '4321', '765432-1')

# transferindo dinheiro
conta_Juan.transferir(1000, conta_Ariany)

# mostrando o histórico de transações
conta_Juan.consultar_historico_transacoes()
conta_Ariany.consultar_historico_transacoes()

print('Saldo Final')
conta_Juan.consultar_saldo()
conta_Ariany.consultar_saldo()

help(ContaCorrente)