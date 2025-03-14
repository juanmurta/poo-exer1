# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

# classes
class TV:

    def __init__(self, mark):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10
        self.marca = mark

    def mudar_canal(self):
        self.canal = 'Disney+'

    def alterar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f'Canal altera para o {novo_canal}')


# programa
tv_sala = TV(mark='samsung')
tv_quarto = TV('aoc')

tv_sala.cor = 'Branca'

print(tv_sala.cor)
print(tv_quarto.canal)

tv_quarto.tamanho = 32
print(tv_quarto.tamanho)
print(tv_sala.tamanho)

print(tv_sala.canal)
tv_sala.mudar_canal()
print(tv_sala.canal)

print(tv_quarto.canal)
tv_quarto.alterar_canal('HBO')
print(tv_quarto.canal)

tv_quarto = TV(mark='samsung')
tv_sala = TV(mark='LG')
print(tv_sala.marca)
print(tv_quarto.marca)


print('-' * 50)


class Vendedor:

    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
        self.meta = 500
        self.bonus = 0

    def vendeu(self, quantidade_vendas):
        self.vendas = quantidade_vendas
        self.calcular_bonus()

    def calcular_bonus(self):
        if self.vendas > self.meta:
            self.bonus = 30
        else:
            self.bonus = 0


vendedor1 = Vendedor('Juan')
vendedor1.vendeu(1500)

vendedor2 = Vendedor('Ariany')
vendedor2.vendeu(300)

print(vendedor1.nome, vendedor2.nome)
print(vendedor1.vendas, vendedor2.vendas)
print(vendedor1.bonus, vendedor2.bonus)