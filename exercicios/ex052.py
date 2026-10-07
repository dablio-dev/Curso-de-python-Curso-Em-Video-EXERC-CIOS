n1 = int (input('Digite um numero inteiro: '))
div = 0
for c in range (1,n1 + 1):
    if n1 % c != 0:
        print(f'\033[1;33m{c}\033[m', end =' ')
    else: # n1 % c == 0
        print(f'\033[1;32m{c}\033[m', end = ' ')
        div += +1
print('\n')
if div == 2:
    print (f'O numero {n1} foi divisivel {div} vezes, ele é um numero primo')
else:
    print(f'O numero {n1} foi divisivel {div} vezes, ele  não é um numero primo')