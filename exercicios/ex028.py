from random import randint
from time import sleep
computador = randint (0,5)
print ('-=-'*20)
print ('Vou pensar em um numero entre 0 e 5 tente advinhar ')
print ('-=-'*20)
usuario = int (input('Digite um numero :'))
print ('PROCESSANDO ...')
sleep (3)
if usuario == computador:
    print (f'Voce acertou eu pensei no numero {computador}')
else:
    print (f'Voce errou eu pensei no numero {computador} e não no numero {usuario}')
