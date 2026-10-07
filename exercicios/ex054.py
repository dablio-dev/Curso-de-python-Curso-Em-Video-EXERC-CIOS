from time import sleep
from datetime import date
cont_maior = 0
cont_menor = 0
ano = date.today().year

for c in range (1, 8):
    nasc = int (input(f'Em que ano a {c}ª pessoa nasceu ?: '))
    idade = ano - nasc
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
sleep(2)
print(f'\nNesta lista {cont_maior} pessoas são maiores de idade!'
      f'\nE outras {cont_menor} pessoas são menores de idade!')

