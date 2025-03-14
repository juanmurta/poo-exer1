from ContasBancos import ContaCorrente, CartaoCredito
from Agencias import AgenciaVirtual, AgenciaComum, AgenciaPremium
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

print('-' * 50 + '\nModulo Cartao de credito')

cartao_Juan = CartaoCredito('Juan', conta_Juan)
print(cartao_Juan.conta_corrente.num_conta)

print(cartao_Juan.numero)

print(cartao_Juan.cod_seguranca)

print(cartao_Juan.validade)

cartao_Juan.senha = '1234'
print(cartao_Juan.senha)

print(conta_Juan.__dict__)
print(cartao_Juan.__dict__)

print('-' * 50 + '\nAgencia Geral')

agencia_premium = AgenciaPremium('11116666', '12345678908765')
agencia_premium.adicionar_cliente('Juan', '12345678900', 50000000)
agencia_premium.verificar_caixa()
print(agencia_premium.clientes)
