contador = soma = 0
while True:
    numero = int(input('Digite um numero inteiro: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'''Quantidade de números digitados: {contador}
Soma entre todos eles: {soma}''')
