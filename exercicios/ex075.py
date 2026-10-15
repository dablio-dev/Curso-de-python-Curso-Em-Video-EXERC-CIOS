numeros_tupla = (int(input('Digite um numero: ')),
                 int(input('Digite outro numero:')),
                 int(input('Digite mais um numero: ')),
                 int(input('Digite o ultimo numero: ')),)
pares = ()
for c in numeros_tupla:
    if c % 2 == 0:
        pares = pares + (c,)
if pares == ():
    pares = (0,)
print(f'O numero 9 apareceu: {numeros_tupla.count(9)} vez(es)')
print(f'O primeiro valor 3 foi digitado na posição: {numeros_tupla.index(3)}' if 3 in numeros_tupla
      else 'O numero 3 não foi digitado')
print('Os valores pares digitados foram: ' , end='')
for numeros in pares:
    print(f'{numeros}', end=' ')