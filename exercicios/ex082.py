lista = list()
pares = list()
impares = list()
while True:
    while True:
        try:
            lista.append(int(input('Digite um numero: ')))
            break
        except ValueError:
            print('Digite um numero inteiro valido!')
            continue

    while True:
        continua = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
        if continua in 'sn':
            break
        else:
            print('Digite uma opção valida!')
    if continua == 'n':
        break

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('-' * 60)
print('A lista completa: ', end='')
print(*lista, sep=', ')

if len(pares) > 0:
    print('A lista de pares é: ', end='')
    print(*pares, sep=', ')
else:
    print('Não existem números pares na lista!')

if len(impares) > 0:
    print('A lista de impares é: ',end='')
    print(*impares, sep=', ')
else:
    print('Não existem números impares na lista!')
