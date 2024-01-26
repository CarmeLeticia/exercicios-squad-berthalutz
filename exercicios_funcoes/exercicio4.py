'''
 Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21

Responsável: Carme
'''

dinheiro = float(input('Digite o valor em carteira: '))

conversao_dolar = dinheiro / 4.91
conversao_peso = dinheiro / 0.02
conversao_dolar_australiano = dinheiro / 3.18
conversao_dolar_canadense = dinheiro / 3.64
conversao_franco_suiço = dinheiro / 0.42
conversao_euro = dinheiro / 5.36
conversao_libra = dinheiro / 6.21

print('Com {} reais você consegue comprar US$ {:.2f} dolares'.format(dinheiro,conversao_dolar))
print('Com {} reais você consegue comprar $ {:.2f} pesos argentinos'.format(dinheiro,conversao_peso))
print('Com {} reais você consegue comprar A$ {:.2f} dolares australianos'.format(dinheiro,conversao_dolar_australiano))
print('Com {} reais você consegue comprar C$ {:.2f} dolares canadenses'.format(dinheiro,conversao_dolar_canadense))
print('Com {} reais você consegue comprar CHF {:.2f} franco suiço'.format(dinheiro,conversao_franco_suiço))
print('Com {} reais você consegue comprar $ {:.2f} euros'.format(dinheiro,conversao_euro))
print('Com {} reais você consegue comprar $ {:.2f} libra esterlina'.format(dinheiro,conversao_libra))