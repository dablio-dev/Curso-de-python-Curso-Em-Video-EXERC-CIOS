print('Gerador de PA'.center(30,' '))
print('-=' * 15)
n1 = int(input('Termo para uma PA: '))
n2 = int(input('Razão para uma PA: '))
n3 = int(input('Numero de razões para uma PA:'))
print('-=' * 15)
contador = 0
soma = n1
while contador < n3:
    print(f'{soma}', end='')
    print(f' → ' if contador < n3 - 1 else '', end='')
    soma += n2
    contador += 1
