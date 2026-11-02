lista = list()

for c in range (1,6):
    while True:
        try:
            numero = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Digite um numero inteiro valido...')
            continue

    if c == 1 or numero >= lista[-1]:
        lista.append(numero)
        print(f'O numero {lista[-1]} foi adicionado na ultima posição')
    else:
        for pos, num in enumerate(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'O numero {numero} foi adicionado na posição {pos}')
                break

print('-' * 60)
print(f'Os valores digitados em ordem foram {lista}')