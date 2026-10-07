from random import randint
from time import sleep
total_vitorias = 0
print('=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30, ' '))
print('=' * 30)
while True:
    computador = randint(0, 10)
    valor = int(input('Digite um valor: '))
    if valor < 0 or valor > 10:
        while valor < 0 or valor > 10:
            print('Opção \033[1;31mINVALIDA\033[m! Digite uma opção valida de 0 a 10 ...')
            valor = int(input('DIgite um valor: '))
    escolha = str(input('Par ou Ímpar ? [P/I]')).strip().lower()[0]
    if escolha not in 'iIíìîpP':
        while escolha not in 'iIíìîpP':
            print('Opção \033[1;31mINVALIDA\033[m! Digite uma opção valida, par ou ímpar [P/I] ...')
            escolha = str(input('Par ou Ímpar ? [P/I]')).strip().lower()[0]
    resultado = computador + valor
    if escolha in 'iIíìî':
        if resultado % 2 != 0:
            print('-' * 30)
            print(f'''O computador jogou {computador} e você jogou {valor}
Você escolheu IMPAR a soma deu {resultado} o total deu IMPAR''')
            print('Você \033[1;32mVENCEU\033[m!')
            print('Vamos jogar novamente ...')
            print('=' * 30)
            total_vitorias += 1
            sleep(1)
        else:
            print('-' * 30)
            print(f'''O computador jogou {computador} e você jogou {valor}
Você escolheu IMPAR a soma deu {resultado} o total deu PAR''')
            print('Você \033[1;31mPERDEU\033[m')
            break
    if escolha in 'Pp':
        if resultado % 2 == 0:
            print('-' * 30)
            print(f'''O computador jogou {computador} e você jogou {valor}
Você escolheu PAR a soma deu {resultado} o total deu PAR''')
            print('Você \033[1;32mVENCEU\033[m!')
            print('Vamos jogar novamente ...')
            print('=' * 30)
            total_vitorias += 1
            sleep(1)
        else:
            print('-' * 30)
            print(f'''O computador jogou {computador} e você jogou {valor}
Você escolheu PAR a soma deu {resultado} o total deu IMPAR''')
            print('Você \033[1;31mPERDEU\033[m')
            break
print('=' * 30)
print(f'GAME OVER! Você venceu {total_vitorias} vezes. ')
