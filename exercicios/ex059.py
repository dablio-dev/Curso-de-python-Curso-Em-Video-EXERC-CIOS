from time import sleep
opcao = ''
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
while opcao != '5':
    print('-=' * 35)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = str(input('Sua escolha: '))
    if opcao == '1':
        print(f'O resultado é {primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor}')
    elif opcao == '2':
        print(f'O resultado é {primeiro_valor} x {segundo_valor} = {primeiro_valor * segundo_valor}')
    elif opcao == '3':
        if primeiro_valor > segundo_valor:
            print(f'O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor})')
        elif primeiro_valor < segundo_valor:
            print(f'O segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor})')
        else:
            print(f'Os valores ({primeiro_valor}) e ({segundo_valor}) são iguis!')
    elif opcao == '4':
        print('Digite os números novamente: ')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
    elif opcao == '5':
        print('Finalizando ...')
        sleep(2)
    else:
        print('Digite uma opção valida...')
    print('-=' * 35)
print('Fim do programa, volte sempre')
