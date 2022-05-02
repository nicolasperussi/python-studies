# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

list = [
    float(input('Digite o valor do primeiro produto: R$ ')),
    float(input('Digite o valor do segundo produto: R$ ')),
    float(input('Digite o valor do terceiro produto: R$ '))
]

list.sort()

print('Você deve comprar o produto de valor R$ {:.2f}.'.format(list[0]))
