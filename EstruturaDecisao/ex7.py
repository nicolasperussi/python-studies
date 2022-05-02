# Faça um Programa que leia três números e mostre o maior e o menor deles.

list = [
    float(input('Digite o primeiro número: ')),
    float(input('Digite o segundo número: ')),
    float(input('Digite o segundo número: '))
]

list.sort()

print('{} é o menor número.'.format(list[0]))
print('{} é o maior número.'.format(list[2]))
