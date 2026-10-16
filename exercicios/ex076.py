nome_precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,'Transferidor',
               4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 31)
print('LISTAGEM DE PREÇOS'. center(31, ' '))
print('-' * 31)
for c in range(0, len(nome_precos), 2):
    print(f'{nome_precos[c]:.<20}'+'R$', f'{nome_precos[c+1]:<6.2f}'.rjust(6,' '))
print('-' * 31)