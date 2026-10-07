nome=input('Digite seu nome completo: ')
print (f'Nome só com minusculas {nome.lower()}'
       f'\nNome só com maiusculas {nome.upper()}'
       f'\nQuantidade de letras {len(nome) - nome.count(' ')}'
       f'\nQuantidade de letras no primeiro nome {len(nome.split()[0])}')
