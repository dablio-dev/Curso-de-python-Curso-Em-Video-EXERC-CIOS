n1 = float (input('Primeiro segmento: '))
n2 = float (input('Segundo segmento: '))
n3 = float (input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('equilátero')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
        print ('isósceles')
    elif n1 != n2 != n3 != n1:
        print('escaleno')
else:
    print('Não podem formar um triângulo')
