# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Digite a letra: ').lower()

if letra == 'f':
    print('{} corresponde ao sexo feminino.'.format(letra.upper()))
elif letra == 'm':
    print('{} corresponde ao sexo masculino.'.format(letra.upper()))
else:
    print('Sexo inválido: {} não corresponde a nenhum sexo.'.format(letra))