n1 = int (input('Primeiro numero: '))
n2 = int (input('Segundo numero: '))

if n1 > n2:
    print (f'O primeiro numero ({n1}) é maior!')
elif n2 > n1:
    print(f'O segundo numero ({n2}) é maior!')
else:
    print(f'Não existe numero maior, os numeros são iguais!')
