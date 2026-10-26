listanum = list()
while True:
    while True:
        try:
            num = (int(input('Digite um numero: ')))
            break
        except ValueError:
            print('Digite um numero inteiro valido!')
            continue
    if num in listanum:
        print('Este numero já esta na lista, não irei adicionar!')
    else:
        listanum.append(num)
        print('Numero adicionado com sucesso!')
    while True:
        continua = str(input('Quer continuar? [S/N]').lower().strip()[0])
        if continua in 'sn':
            break
        else:
            print('Digite uma opção valida [S/N].')
    if continua == 'n':
        break
    elif continua == 's':
        continue
listanum.sort()
print('-' * 30)
print('Sua lista ordenada de forma crescente: ', end='')
for pos, valor in enumerate(listanum):
    print(f'{valor}', end='')
    if pos < len(listanum) - 1:
        print(', ', end='')