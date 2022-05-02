# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

val = float(input('Digite um valor: '))

if val > 0:
    print('O valor é positivo.')
elif val < 0:
    print('O valor é negativo.')
else:
    print('O valor é nulo.')
