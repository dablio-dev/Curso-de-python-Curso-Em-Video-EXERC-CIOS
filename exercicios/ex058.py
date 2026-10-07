from random import randint
from time import sleep

pc = randint(1,10)
tentativas = 0
acertou = False

print(' Jogo de adivinhação '.center(50, '-'))
print('Adivinhe o numero de 1 a 10 que o pc pensou'. center(50,' '))
sleep(1)

while not acertou:
    print('-' * 50)
    player = int(input('Escolha um numero inteiro de 1 a 10: '))
    if player == pc:
        acertou = True
    else:
        if player < pc:
            print('Você errou! tente novamente com um chute mais alto! ...')
        else:
            print('Você errou! Tente novamente com um chute mais baixo! ...')
    tentativas += 1

print('-' * 50)
if tentativas <= 1:
    print(f'Parabens! Acertou de primeira o computador pensou {pc}')
else:
    print(f'Com {tentativas} tentativas você acertou, o computador pensou {pc}')
print('-' * 50)