lista = list()
while True:
    while True:
        try:
            lista.append(int(input('Digite um valor: ')))
            break
        except ValueError:
            print('Digite um numero inteiro valido...')
            continue
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
        if continua == 's' or continua == 'n':
            break
        else:
            print('Digite uma opção valida para [S/N]')
    if continua == 'n':
        break

lista.sort(reverse=True)
print('-' * 60)
print(f'Você digitou {len(lista)} valores.')
print('Os valores em ordem decrescente são: ', end='')
for pos, valor in enumerate(lista):
    print(f'{valor}', end='')
    if pos < len(lista) - 1:
        print(f', ', end='')

if 5 in lista:
    print('\nO valor 5 está na lista!')
else:
    print('\nO valor 5 não está na lista!')