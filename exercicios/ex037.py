numero = int (input ('Digite um numero inteiro: '))
metodo = input('[ 1 ] Binario'
               '\n[ 2 ] Octal'
               '\n[ 3 ] Hexadecimal'
               '\nSua escolha: ')

convert = 0
msg = 0

if metodo == '1':
    convert = bin(numero)
    msg = 'BINARIO'
elif metodo == '2':
    convert = oct(numero)
    msg = 'OCTAL'
elif metodo == '3':
    convert = hex(numero)
    msg = 'HEXADECIMAL'
else:
    msg = 'x'
if msg == 'x':
    print('\033[1;31mOpção invalida!\033[m')
else:
    print(f'O numero {numero} convertido para {msg} é igual a {convert[2:]}')
