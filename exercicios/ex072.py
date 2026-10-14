numeros = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    try:
        entrada_usuario = int(input('Digite um numero entre 0 e 20: '))
        if entrada_usuario < 0 or entrada_usuario > 20:
            print('Digite um valor valido ...')
            continue
    except ValueError:
        print('Digite um valor valido ...')
        continue
    print(f'Você digitou o numero {numeros[entrada_usuario]}')
    continua = str(input('Você quer continuar? [S/N]: ')).strip()[0]
    while continua not in 'SsNn':
        print('Digite uma opção valida ...')
        continua = str(input('Você quer continuar? [S/N]: ')).strip()[0]
    if continua in 'Nn':
        break