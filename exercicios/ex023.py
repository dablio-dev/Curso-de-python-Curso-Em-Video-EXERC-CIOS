n1=int (input('Digite um numero de 0 a 9999: '))
n2=f'{n1:04d}'
print (f'o numero {n1} tem...'
       f'\nUnidades {n2[3]}'
       f'\nDezenas {n2[2]}'
       f'\nCentenas {n2[1]}'
       f'\nMilhares {n2[0]}')