s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print (f'A soma entre todos os valores são {s} foram somados o total de {cont} valores')

#tive dificuldade e precisei "copiar" o professor, eu tive dificuldade nos acumuladores e contadores, ainda não entendi muito bem a logica do for
