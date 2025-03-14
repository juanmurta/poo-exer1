from datetime import datetime
import pytz
from random import randint


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
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """
            Exibe o saldo atual da conta do cliente.
            Não possui parâmetros.
        """
        print(f'{self.nome} Seu saldo atual é de R$ {self._saldo:.2f}')

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


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self._senha = None
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Senha inválida')

