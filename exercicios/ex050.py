s = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Fora digitados {cont} numeros pares e soma entre todos os numeros pares da lista é {s}')