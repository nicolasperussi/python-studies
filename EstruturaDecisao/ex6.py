# Faça um Programa que leia três números e mostre o maior deles.

list = [
    float(input('Digite o primeiro número: ')),
    float(input('Digite o segundo número: ')),
    float(input('Digite o segundo número: '))
]

list.sort()

print('{} é o maior número.'.format(list[2]))
