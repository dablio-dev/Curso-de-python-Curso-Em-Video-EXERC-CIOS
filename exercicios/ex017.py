from math import hypot
'''from math import sqrt
oposto=float(input('Comprimento do cateto oposto: '))
adjacente=float(input('Comprimento do cateto adjacente: '))
result=oposto**2 + adjacente**2
print ('A hipotenusa vai medir {:.2f}'.format(sqrt(result)))'''

oposto=float(input('Comprimento do cateto oposto: '))
adjacente=float(input('Comprimento do cateto adjacente: '))
hypo=hypot(oposto, adjacente)
print (f'A hipotenusa vai medir {hypo:.2f}')
