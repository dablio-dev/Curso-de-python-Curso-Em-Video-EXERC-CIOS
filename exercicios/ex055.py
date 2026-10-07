pesomaior = 0
pesomenor = 0
for c in range (1,6):
    peso = float(input(f'Peso da {c}ª pessoa ? '))
    if c == 1:
        pesomenor = peso
        pesomaior = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        elif peso < pesomenor:
            pesomenor = peso
print(f'\nO maior peso lido foi: {pesomaior:.1f}Kg'
      f'\nO menor peso lido foi: {pesomenor:.1f}Kg')
