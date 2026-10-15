from random import sample
numeros_sorteados = tuple(sample (range(0,10),5))
print (f'Os 5 números sorteados foram... {numeros_sorteados[0:]}')
print('-' * 15)
for numero in numeros_sorteados:
    print(numero, end='')
print('\n'+'-' * 15)
print(f'Maior número do sorteio: {max(numeros_sorteados)}')
print(f'Menor número sorteado foi: {min(numeros_sorteados)}')


