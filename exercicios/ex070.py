print('-' * 30)
print('Mercearia Dablio'.center(30, ' '))
print('-' * 30)

total_gasto = mais_mil = mais_barato = contador = 0
barato_nome = ''
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = ' '
    while type(preco) != float:
        try:
            preco = float(input('Preço do produto: '))
        except ValueError:
            preco = ' '
    if contador == 0 or preco < mais_barato:
        mais_barato = preco
        barato_nome = nome
    contador += 1
    total_gasto += preco
    if preco > 1000:
        mais_mil += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'Nn':
        break
print(' FIM DO PROGRAMA '.center(30, '-'))
print(f'''Total da compra foi | R$ {total_gasto:.2f}
Produtos custando mais de R$ 1000.00 | {mais_mil}
Produto mais barato | {barato_nome} R$ {mais_barato:.2f}''')