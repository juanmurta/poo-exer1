class ContaCorrente:

    def __init__(self, nome, cpf):
        self.limite = None
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R$ {self.saldo:.2f}')

    def depositar(self, valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Saldo insuficiente')
            self.consultar_saldo()
        else:
            self.saldo -= valor


# programa
conta_juan = ContaCorrente('Juan', '123.456.789-00')
conta_juan.consultar_saldo()


# depositando dinheiro na conta
conta_juan.depositar(10000)
conta_juan.consultar_saldo()

# sacando dinheiro da conta
conta_juan.sacar_dinheiro(10500)
conta_juan.consultar_saldo()
