valor = float (input('Valor do produto: R$ '))
print(' FORMAS DE PAGAMENTO '.center(60, '='))
print('''[ 1 ] dinheiro
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = input('Sua opção: ')
if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
    print(f'A opção {opcao} na forma de pagamento é \033[1;31mINVALIDA\033[m')
else:
    calculo = 0
    final = 0
    msg = 0
    parcelas = 1

    if opcao == '1':
        calculo = valor / 100 * 10
        final = valor - calculo
        msg = '10% de desconto'
    elif opcao == '2':
        calculo = valor / 100 * 5
        final = valor - calculo
        msg = '5% de desconto aplicado'
    elif opcao == '3':
        final = valor
        parcelas = 2
        msgparcelas = final / parcelas
        msg = 'preço normal'
    elif opcao == '4':
        parcelas = int (input('Quantas parcelas ? (max 12): '))
        calculo = valor / 100 * 20
        final = valor + calculo
        msg = '20% de juros'
        msgparcelas = final / parcelas
    msgparcelas = final / parcelas
    print('\n')
    print(' Recibo '.center(35, '='))
    print(f'''Valor do produto: R$ {valor:.2f}
Foi aplicado: {msg}
Numero de parcelas: {parcelas}
Valor das parcelas: R$ {msgparcelas:.2f}
A alteração no valor foi: R$ {calculo:.2f}
Valor total: \033[1;32mR$ {final:.2f}\033[m ''')
    print('=' * 35)
