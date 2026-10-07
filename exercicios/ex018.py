from math import radians, sin, cos, tan
angulo=float(input('Digite o angulo que você deseja: '))
rad=radians(angulo)
seno=sin(rad)
cosseno=cos(rad)
tangente=tan(rad)
print ('O angulo de {:.2f} tem o SENO {:.2f}: '.format(angulo, seno))
print (f'O angulo de {angulo:.2f} tem o cosseno {cosseno:.2f}:')
print (f'O angulo de {angulo:.2f} tem a tangente {tangente:.2f}: ')
