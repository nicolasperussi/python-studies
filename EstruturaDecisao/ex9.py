# Faça um Programa que leia três números e mostre-os em ordem decrescente.

list = [
    float(input('Digite o primeiro valor: ')),
    float(input('Digite o segundo valor: ')),
    float(input('Digite o terceiro valor: '))
]

list.sort(reverse=True)

string_list = [str(number) for number in list]

print('Números em ordem decrescente: {}.'.format(', '.join(string_list)))
