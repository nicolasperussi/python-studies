# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ').lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('{} é uma vogal.'.format(letra))
else:
    print('{} é uma consoante.'.format(letra))
