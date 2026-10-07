nome=str(input('Digite seu nome completo: '))
split=nome.split()
print (f'Olá prazer em te conhecer'
       f'\nSeu primeiro nome é {split[0]}'
       f'\nSeu ultimo nome é {split[len(split) - 1]}')
