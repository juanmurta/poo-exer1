class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nivel recomendado. Caixa Atual: R$ {self.caixa:.2f}')
        else:
            print('O valor de caixa está dentro do recomendado. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Caixa sem saldo para emprestimos')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=2000)
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=3000)
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não atende aos requisitos para ser cliente premium')


if __name__ == '__main__':
    print('-' * 50 + 'Agencia Geral')
    agencia1 = Agencia('11113333', '12345678901234', '4568')
    agencia1.caixa = 1000000
    agencia1.verificar_caixa()
    agencia1.emprestar_dinheiro(100000, '12345678900', 0.1)

    print('-' * 50 + 'Agencia Virtual')
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com', '12345678904321', '12345678901234')
    agencia_virtual.verificar_caixa()
    agencia_virtual.depositar_paypal(20000)
    agencia_virtual.sacar_paypal(10000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    print('-' * 50 + 'Agencia Comum')
    agencia_comum = AgenciaComum('11115555', '12345678905678')
    agencia_comum.verificar_caixa()
    agencia_comum.adicionar_cliente('Ariany', '12345678900', 100000)
    print(agencia_comum.clientes)

    print('-' * 50 + 'Agencia Premium')
    agencia_premium = AgenciaPremium('11116666', '12345678908765')
    agencia_premium.adicionar_cliente('Juan', '12345678900', 50000000)
    agencia_premium.verificar_caixa()
    print(agencia_premium.clientes)
