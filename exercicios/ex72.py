numeros = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    try:
        entrada_usuario = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= entrada_usuario <= 20:
            break
        else:
            print('Digite um valor valido ...')
            continue
    except ValueError:
        print('Digite um valor valido ...')
        continue
print(f'Você digitou o numero {numeros[entrada_usuario]}')
