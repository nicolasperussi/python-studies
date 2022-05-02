# Faça um Programa que peça dois números e imprima o maior deles.

val1 = float(input('Digite o primeiro valor: '))
val2 = float(input('Digite o segundo valor: '))

if val1 > val2:
    print('O maior valor é {}'.format(val1))
else:
    print('O maior valor é {}'.format(val2))
