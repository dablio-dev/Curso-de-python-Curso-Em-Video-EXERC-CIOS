'''from calendar import isleap
ano = int (input ('digite um ano e descubra se ele é bissexto: '))
result = str (isleap (ano))
if result == 'True':
    print (f'O ano {ano} é bissexto!')
else:
    print (f'O ano {ano} não é bissexto!')'''
from datetime import date
ano = int (input ('Digite um ano para saber se ele é bissexto, digite 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano {ano} é um ano BISSEXTO')
else:
    print (f'O ano {ano} não é um ano BISSEXTO')
