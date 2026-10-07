from random import choice
opcao = ['pedra', 'papel', 'tesoura']

player = input('Pedra, papel ou tesoura ?: ').strip().lower()

if player != 'pedra' and player != 'papel' and player != 'tesoura':
    print('Escolha uma opção valida')
else:
    pc = choice(opcao)
    vencedor = 'Empate'
    if pc == 'pedra' and player == 'tesoura':
        vencedor = 'vitoria pc'
    elif pc == 'papel' and player == 'pedra':
        vencedor = 'vitoria pc'
    elif pc == 'tesoura' and player == 'papel':
        vencedor = 'vitoria do pc'
    elif pc == player:
        vencedor = 'empate'
    else:
        vencedor = 'vitoria do jogador'
    print(f'O pc escolheu {pc} e o jogador escolheu {player} o resultado foi {vencedor}')
