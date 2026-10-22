valores = list()
for c in range (1, 6):
    while True:
        try:
            valores.append(int(input(f'Digite o {c}º valor: ')))
            break
        except ValueError:
            print('Digite um valor inteiro valido...')
            continue
maiores_index = list()
menores_index = list()
maior_valor = max(valores)
menor_valor = min(valores)
print('-' * 50)
print('Tratamento de dados'.upper().center(50,' '))
print('Você digitou os valores: ', end='')
for cont, valor in enumerate(valores):
    print(f'{valor}', end='')
    if cont < 4:
        print(', ', end='')
    if valor == maior_valor:
        maiores_index.append(cont)
    if valor == menor_valor:
        menores_index.append(cont)
print(f'\nMaior valor digitado: {maior_valor} | Posições na lista: ', end='')
for cont, index in enumerate(maiores_index):
    print(f'{index + 1}', end='')
    if cont < len(maiores_index) - 1:
        print(', ', end='')
print(f'\nMenor valor digitado: {menor_valor} | Posições na lista: ', end='')
for cont, index in enumerate(menores_index):
    print(f'{index + 1}', end='')
    if cont < len(menores_index) - 1:
        print(', ', end='')
print('\n','-' * 50)
